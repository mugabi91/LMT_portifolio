import re
import time
from pathlib import Path

import nbformat
import pandas as pd
import streamlit as st
from pydantic import BaseModel


def render_component(file_path: str, context: BaseModel) -> str:
    """
    Reads an HTML file and replaces {{key}} placeholders 
    dynamically using a Pydantic model.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Convert model to dict once
        data = context.model_dump()
    
        # Use a single regex pass to replace all placeholders
        # This looks for {{ key }} and uses the key to look up the value in our dict
        pattern = r"\{\{\s*(\w+)\s*\}\}"
        
        def replace_match(match):
            key = match.group(1)
            # Returns the value if key exists, otherwise keeps the {{placeholder}}
            return str(data.get(key, match.group(0)))

        return re.sub(pattern, replace_match, html_content)

    except FileNotFoundError:
        return "Error: HTML file not found."
    except Exception as e:
        return f"Error: {str(e)}"


#function to create type write effect
def stream_data(body:str):
    for word in body.split(" "):
        yield word + " "
        time.sleep(0.02)


# function to read jupyter files
def read_and_display_jupyter_file(notebook_path: Path):
    # Ensure it's a resolved absolute path object
    absolute_path = notebook_path.resolve()

    # Debug sanity check: print directly to your terminal to verify the actual location
    print(f"Attempting to read notebook from: {absolute_path}")

    try:
        with open(absolute_path, "r", encoding="utf-8") as nb_file:
            notebook = nbformat.read(nb_file, as_version=4)

        # Extract and render cells
        for cell in notebook.cells:
            if cell.cell_type == "markdown":
                st.markdown(cell.source)
            elif cell.cell_type == "code":
                # Render the input code block
                st.code(cell.source, language="python")

                # Optional: Render text stream outputs (like print statements) if they exist
                if "outputs" in cell:
                    for output in cell.outputs:
                        if (
                            output.output_type == "stream"
                            and "text" in output
                        ):
                            st.text(output.text)

    except FileNotFoundError:
        # FIX: Directly render the error to the UI so you can see it
        st.error(f"❌ Jupyter Notebook file not found at: {absolute_path}")
    except Exception as e:
        # FIX: Directly render any parsing or system errors to the UI
        st.error(f"❌ Error rendering notebook: {str(e)}")



# function to read datasets
def read_file(file_location:str):
    supported_file_types: list[str] = [
    ".xlsx",  # Excel Workbook (XML-based)
    ".xlsm",  # Excel Macro-Enabled Workbook (XML-based)
    ".xls",   # Excel 97-2003 Workbook (Binary-based)
    ".csv",   # Comma Separated Values
    ".xltx",  # Excel Template (XML-based)
    ".xltm",  # Excel Macro-Enabled Template (XML-based)
    ".xlsb",  # Excel Binary Workbook
    ".ods"    # OpenDocument Spreadsheet
]
    
    file_type: str = file_location.split(".")[-1].lower()
    if file_type in supported_file_types:
        df: pd.DataFrame = pd.read_excel(file_location) # type: ignore
        return df 
    else:
        match file_type:
            case "csv":
                df = pd.read_csv(file_location) # type: ignore
                return df 
            case "json":
                df = pd.read_json(file_location) # type: ignore
                return df

            case "parquet":
                df = pd.read_parquet(file_location) 
            case _ :
                print(f">>>[Error Info]:File type unsupported..")
                return None



def render_course_template(
    course_title: str, folder_name: str, page_title: str, icon_path: str
):
    """Universal template to render any notebook-based course layout with a

    sticky right sidebar and back-to-top navigation.
    """
    st.set_page_config(
        page_title=page_title,
        layout="wide",
        page_icon=icon_path,
    )

    # 1. Invisible HTML anchor target link placed at index 0 of the DOM
    st.markdown("<div id='top-anchor'></div>", unsafe_allow_html=True)

    # Inject Universal CSS Layout Engine
    st.markdown(
        """
        <style>

        /* =========================
        BASE RESET / SAFETY
        ========================= */

        html, body {
            overflow-x: hidden;
        }

        /* =========================
        MAIN LAYOUT WRAPPER
        (Streamlit columns override-safe)
        ========================= */

        div[data-testid="stHorizontalBlock"]{
            gap: 2rem;
        }

        /* =========================
        LEFT COLUMN (MAIN CONTENT)
        ========================= */

        div[data-testid="stHorizontalBlock"] > div:first-child {
            flex: 1 1 75% !important;
            max-width: 75% !important;
            padding-right: 3rem;
            box-sizing: border-box;
        }

        /* =========================
        RIGHT COLUMN (SIDEBAR)
        ========================= */

        div[data-testid="stHorizontalBlock"] > div:nth-child(2) {
            position: fixed;
            right: 0;
            top: 0;
            height: 100vh;

            width: 18%;
            min-width: 260px;

            overflow-y: auto;

            padding: 6rem 1.5rem 2rem 1.5rem;

            background: rgba(255,255,255,.35);
            backdrop-filter: blur(24px);

            border-left: 1px solid rgba(255,255,255,.8);
            box-shadow: -10px 0 40px rgba(0,0,0,.05);

            z-index: 99;
        }

        /* =========================
        BACK TO TOP BUTTON
        ========================= */

        .scroll-top-btn {
            position: fixed;
            bottom: 2rem;
            left: 2rem;

            background-color: #2563eb;
            color: white !important;

            padding: 0.6rem 1rem;
            border-radius: 999px;

            font-weight: 600;
            font-size: 0.85rem;

            box-shadow: 0 10px 25px rgba(0,0,0,0.15);
            z-index: 1000;

            transition: 0.2s ease;
        }

        .scroll-top-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 15px 30px rgba(37,99,235,0.25);
        }

        /* =========================
        RESPONSIVE FIX (MOBILE)
        ========================= */

        @media (max-width: 768px){

            /* stack layout */
            div[data-testid="stHorizontalBlock"]{
                flex-direction: column !important;
            }

            /* left column full width */
            div[data-testid="stHorizontalBlock"] > div:first-child {
                max-width: 100% !important;
                padding-right: 0 !important;
            }

            /* sidebar becomes normal flow */
            div[data-testid="stHorizontalBlock"] > div:nth-child(2) {
                position: relative !important;
                width: 100% !important;
                height: auto !important;

                margin-top: 2rem;

                border-left: none;
                border-radius: 16px;

                box-shadow: 0 10px 30px rgba(0,0,0,.08);
            }

            /* move back-to-top button */
            .scroll-top-btn {
                bottom: 1rem;
                left: 1rem;
                font-size: 0.8rem;
                padding: 0.5rem 0.9rem;
            }
        }

</style>
        """,
        unsafe_allow_html=True,
    )

    # Dynamic Path Resolution based on the provided folder name
    CURRENT_DIR = Path(__file__).resolve().parent
    PARENT_DIR = CURRENT_DIR.parent
    location = PARENT_DIR / "Learn" / folder_name

    # Safely find and sort files
    notebook_files = sorted(list(location.glob("*.ipynb")))

    if not notebook_files:
        st.error(
            f"❌ No notebooks found in the directory: `Learn/{folder_name}`"
        )
        return

    # Clean display mapping engine
    file_display_map = {
        file.name.replace(".ipynb", "").replace("_", " "): file
        for file in notebook_files
    }

    st.write(f"# {course_title}")
    st.divider()

    # Create the column distribution split
    doc_col, nav_col = st.columns([5, 1], gap="large")

    with nav_col:
        st.markdown("### Course Contents")
        selected_display_name = st.radio(
            "Select a Module:",
            options=list(file_display_map.keys()),
            label_visibility="collapsed",
        )

    with doc_col:
        st.markdown(f"### 📑 Active Module: *{selected_display_name}*")

        selected_file_path = file_display_map[selected_display_name]
        read_and_display_jupyter_file(selected_file_path)

        st.markdown("<div class=col2><div>", unsafe_allow_html=True)
        st.divider()

    # Inject floating action link back to top
    st.markdown(
        '<a href="#top-anchor" class="scroll-top-btn">⬆ Back to Top</a>',
        unsafe_allow_html=True,
    )

