import re
import time

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
def read_and_display_jupyter_file(notebook_path:str):#type: ignore
    try:
        with open(notebook_path, "r",encoding="utf-8") as nb_file:#type: ignore
            notebook = nbformat.read(nb_file, as_version=4) # type: ignore
        # Extract cell outputs
        for cell in notebook.cells: # type: ignore
            if cell.cell_type == "markdown": # type: ignore
                st.markdown(cell.source)  # type: ignore
            elif cell.cell_type == "code": # type: ignore
                st.code(cell.source) # type: ignore
    except FileNotFoundError:
        return f"Error: Jupyter Notebook file not Found {notebook_path}"
    except Exception as e:
        return f"Error: {str(e)}"



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
