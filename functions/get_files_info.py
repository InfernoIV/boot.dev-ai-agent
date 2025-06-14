import os

def get_files_info(working_directory, directory=None):

    #print(f"get_files_info: '{working_directory}', '{directory}'")
    absolute_path = os.path.abspath(working_directory)
    joined_path = os.path.join(absolute_path, directory)
    abs_path = os.path.abspath(joined_path)
    #print(f"absolute_path: '{absolute_path}', joined_path: '{joined_path}', abs_path: '{abs_path}'")


    #If the directory argument is outside the working_directory, return a string with an error:
    if not abs_path.startswith(absolute_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    #If the directory argument is not a directory, again, return an error string:
    if not os.path.isdir(abs_path):
        return f'Error: "{directory}" is not a directory'
    
    #If any errors are raised by the standard library functions, catch them and instead return a string describing the error. Always prefix error strings with "Error:".
    try:
        directory_contents = os.listdir(abs_path)
        #print(f"directory_contents: {directory_contents}")
        file_information = []
        for content in directory_contents:
            file_path = os.path.join(abs_path, content)
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
    