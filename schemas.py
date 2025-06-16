from google import genai
from google.genai import types


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


schema_get_file_content= types.FunctionDeclaration(
    name="get_file_content",
    description="Read content of a file, turnicated to 10000 characters, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to list the content of, relative to the working directory.",
            ),
        },
    ),
)


schema_run_python_file= types.FunctionDeclaration(
    name="run_python_file",
    description="Run script with arguments in the specified directory, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The python script file, relative to the working directory.",
            ),
        },
    ),
)


schema_write_file= types.FunctionDeclaration(
    name="write_file",
    description="(over)writes files in the specified directory aoccording to the specified content, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="the specified file in the directory, constrained to the working directory.",
            ),"content": types.Schema(
                type=types.Type.STRING,
                description="Content to write",
            ),
        },
    ),
)



available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)