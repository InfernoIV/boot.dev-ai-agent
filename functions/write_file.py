import os
from functions.check_path import check_path


result = str


def write_file(working_directory: str, file_path: str, content: str) -> result:

    path, error = check_path(working_directory, file_path, "write")
    if error != None:
        return error
    
    #get only the directory
    directory = os.path.dirname(path)
    
    #Check if a path exists
    if not os.path.exists(directory): 
        #Create a directory and all its parents
        os.makedirs(directory)

    try :

        #Overwrite the contents of the file with the content argument.
        with open(path, "w") as f:
            characters_written = f.write(content)

            #If successful, return a string with the message:
            if characters_written == len(content):
                return f"Successfully wrote to \"{file_path}\" ({len(content)} characters written)"
            else: 
                return f"Error: could not write all characters to \"{file_path}\": only {characters_written} of {len(content)} character written"
        
    except Exception as inst:
        return f"Error: {inst}"
    