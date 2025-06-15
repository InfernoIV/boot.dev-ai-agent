import os

def get_file_content(working_directory, file_path):
    #print(f"get_files_info: '{working_directory}', '{directory}'")
    absolute_path = os.path.abspath(working_directory)
    joined_path = os.path.join(absolute_path, file_path)
    abs_path = os.path.abspath(joined_path)
    #print(f"absolute_path: '{absolute_path}', joined_path: '{joined_path}', abs_path: '{abs_path}'")
    
    #If the file_path is outside the working_directory, return a string with an error:
    if not abs_path.startswith(absolute_path): 
        return f'Error: Cannot read "{abs_path}" as it is outside the permitted working directory'

    #If the file_path is not a file, again, return an error string:
    if not os.path.isfile(abs_path):
        return f'Error: File not found or is not a regular file: "{abs_path}"'
    
    try :
        #Read the file and return its contents as a string.
        MAX_CHARS = 10000
        with open(abs_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)

        #If the file is longer than 10000 characters, truncate it to 10000 characters and append this message to the end:
        if len(file_content_string) >= MAX_CHARS:
            #[...File "{file_path}" truncated at 10000 characters]
            file_content_string += f"[...File \"{abs_path}\" truncated at 10000 characters]"
        
        return file_content_string
    except Exception as inst:
        return f"Error: {inst}"

    #If any errors are raised by the standard library functions, catch them and instead return a string describing the error. Always prefix errors with "Error:".