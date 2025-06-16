import os
from functions.check_path import check_path


result = str


def get_files_info(working_directory: str, directory: str = None) -> result:

    path, error = check_path(working_directory, directory)
    if error != None:
        return error
    
    #If the directory argument is not a directory, again, return an error string:
    if not os.path.isdir(path):
        return f'Error: "{directory}" is not a directory'
    
    #If any errors are raised by the standard library functions, catch them and instead return a string describing the error. Always prefix error strings with "Error:".
    try:
        directory_contents = os.listdir(path)
        #print(f"directory_contents: {directory_contents}")
        file_information = []
        for content in directory_contents:
            file_path = os.path.join(path, content)
            #Build and return a string representing the contents of the directory. It should use this format:
            #- README.md: file_size=1032 bytes, is_dir=False
            #- src: file_size=128 bytes, is_dir=True
            #- package.json: file_size=1234 bytes, is_dir=False
            file_name = content
            file_size = os.path.getsize(file_path)
            is_dir = not os.path.isfile(file_path)
            file_string = f"- {file_name}: file_size={file_size}, is_dir={is_dir}"
            #print(f"file_string: '{file_string}'")
            file_information.append(file_string)

        #print(f"content_string: {"\r\n".join(file_information)}")
        return "\r\n".join(file_information)
    except Exception as inst:
        return f"Error: {inst}"
    