from google.genai.types import FunctionDeclaration, Schema, Type

schema_get_files_info = FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=Schema(
        type=Type.OBJECT,
        properties={
            "directory": Schema(
                type=Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_get_file_content = FunctionDeclaration(
    name="get_file_content",
    description="Reads and returns the contents of a file, limited to 10,000 characters.",
    parameters=Schema(
        type=Type.OBJECT,
        properties={
            "file_path": Schema(type=Type.STRING, description="The path to the file."),
        },
        required=["file_path"],
    ),
)

schema_run_python_file = FunctionDeclaration(
    name="run_python_file",
    description="Runs a Python script file and captures stdout/stderr.",
    parameters=Schema(
        type=Type.OBJECT,
        properties={
            "file_path": Schema(type=Type.STRING, description="The Python file to run."),
        },
        required=["file_path"],
    ),
)

schema_write_file = FunctionDeclaration(
    name="write_file",
    description="Writes content to a file. Overwrites if the file already exists.",
    parameters=Schema(
        type=Type.OBJECT,
        properties={
            "file_path": Schema(type=Type.STRING, description="The path of the file to write."),
            "content": Schema(type=Type.STRING, description="The content to write to the file."),
        },
        required=["file_path", "content"],
    ),
)
