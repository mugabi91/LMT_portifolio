import re

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
