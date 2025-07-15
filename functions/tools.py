from google.genai.types import Tool
from functions.get_files_info import schema_get_files_info 

available_functions = Tool(
    function_declarations=[
        schema_get_files_info,
        # Add more like: schema_write_file, schema_run_python_file, etc.
    ]
)
