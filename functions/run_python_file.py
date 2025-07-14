import os
import subprocess

def run_python_file(working_directory, file_path):
    try: 
        working_abs = os.path.abspath(working_directory)
        target_abs = os.path.abspath((os.path.join(working_directory, file_path or "")))

        if not target_abs.startswith(working_abs):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory' 
        
        if not os.path.isfile(target_abs):
            return f'Error: File "{file_path}" not found.'

        if not target_abs.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file.'

        result = subprocess.run(
                ["python3", target_abs], 
                capture_output=True, 
                text=True, 
                timeout=30
            )

        output_lines = []
        
        if result.stdout.strip():
            output_lines.append(f'STDOUT:\n{result.stdout.strip()}')
        if result.stderr.strip():
            output_lines.append(f'STDERR:\n{result.stderr.strip()}')

        if result.returncode != 0:
            output_lines.append(f'Process exited with code {result.returncode}')

        if not output_lines:
            return 'No output produced'

        return "\n".join(output_lines)

    except Exception as e:
        return f'Error: executing Python file: {str(e)}'
