import os


path = str
error = str


def check_path(working_directory: str, file_path: str, action_type: str) -> tuple[path, error]:
    absolute_path = os.path.abspath(working_directory)
    #if no path specified, return the working directory
    if file_path == None:
        return absolute_path, None

    joined_path = os.path.join(absolute_path, file_path)
    abs_path = os.path.abspath(joined_path)
    #print(f"absolute_path: '{absolute_path}', joined_path: '{joined_path}', abs_path: '{abs_path}'")

    #If the file_path is outside the working_directory, return a string with an error:
    if not abs_path.startswith(absolute_path): 
        return None, f'Error: Cannot {action_type} "{file_path}" as it is outside the permitted working directory'
    #return absolute path, is file and None (no error)
    return abs_path, None
