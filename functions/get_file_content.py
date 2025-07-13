import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:

        working_abs = os.path.abspath(working_directory)
        target_abs = os.path.abspath((os.path.join(working_directory, file_path or "")))

        if not target_abs.startswith(working_abs):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory.'
        
        if not os.path.isfile(target_abs):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(target_abs, "r") as f:
            content = f.read()
            if len(content) > MAX_CHARS:
                return content[:MAX_CHARS] + f'[...File "{file_path}" truncated at {MAX_CHARS}]'
            return content

    except Exception as e:
        return f'Error: {str(e)}'
