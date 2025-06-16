import os
from functions.check_path import check_path


result = str


def get_file_content(working_directory: str, file_path: str) -> result:
        
    path, error = check_path(working_directory, file_path, "read")
    if error != None:
        return error

    if not os.path.isfile(path): 
        return f'Error: File not found or is not a regular file: "{path}"'
    
    try :
        #Read the file and return its contents as a string.
        MAX_CHARS = 10000
        with open(path, "r") as f:
            file_content_string = f.read(MAX_CHARS)

        #If the file is longer than 10000 characters, truncate it to 10000 characters and append this message to the end:
        if len(file_content_string) >= MAX_CHARS:
            #[...File "{file_path}" truncated at 10000 characters]
            file_content_string += f"[...File \"{path}\" truncated at 10000 characters]"
        
        return file_content_string
    except Exception as inst:
        return f"Error: {inst}"

    #If any errors are raised by the standard library functions, catch them and instead return a string describing the error. Always prefix errors with "Error:".