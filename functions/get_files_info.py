import os
from google.genai import types

def get_files_info(working_directory, directory=None):
    try:

        working_abs = os.path.abspath(working_directory)
        target_abs = os.path.abspath((os.path.join(working_directory, directory or "")))

        if not target_abs.startswith(working_abs):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory.'
        
        if not os.path.isdir(target_abs):
            return f'Error: "{directory}" is not a directory'
        
        files = os.listdir(target_abs)
        return_lines = []

        for file in files:
            file_path = os.path.join(target_abs, file)    
            size = os.path.getsize(file_path)
            is_dir = os.path.isdir(file_path)
            return_lines.append(f'{file}: file_size={size} bytes, is_dir={is_dir}')

        return "\n".join(return_lines) if return_lines else "[empty directory]"

    except Exception as e:
        return f'Error: {str(e)}'

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)


