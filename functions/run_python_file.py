import os
import subprocess
from functions.check_path import check_path


result = str


def run_python_file(working_directory: str, file_path: str) -> result:
    #If the file_path is outside the working directory, return a string with an error:
    path, error = check_path(working_directory, file_path, "execute")
    if error != None:
        return error
    
    #If the file_path doesn't exist, return an error string:
    if not os.path.isfile(path): 
        return f'Error: File "{file_path}" not found.'
    
    filename, file_extension = os.path.splitext(path)
    #If the file doesn't end with ".py", return an error string:
    if file_extension != ".py":
        return f'Error: "{file_path}" is not a Python file.'

    #rwxr-xr-x make it executable 
    os.chmod(path, 0b111101101)    
    

    try:
        #Set a timeout of 30 seconds to prevent infinite execution
        #Set the working directory properly (?)
        #Use subprocess.run function to execute the Python file.
        completed_process = subprocess.run(["python3", path], capture_output=True, timeout=30)
        
        #create information storage
        execution_information = []
        #add script information
        execution_information.append(f"Ran \"{path}\"")

        #If no output is produced, return "No output produced."
        if len(completed_process.stdout) == 0:
            #add output
            execution_information.append(f"No output produced.")
            #return information
            return "\r\n".join(execution_information)
        
        
        #add std out
        execution_information.append(f"STDOUT: \"{completed_process.stdout}\"") 
        #add std error
        execution_information.append(f"STDERR: \"{completed_process.stderr}\"")

        #If the process exits with a non-zero code, include "Process exited with code X"
        if completed_process.returncode != 0:
            #add return code
            execution_information.append(f"Process exited with code {completed_process.returncode}")

        #return the values in a formatted way
        return "\r\n".join(execution_information)
    
    #If any exceptions occur during execution, catch them and return an error string:
    except Exception as inst:
        #return error value
        return f"Error: executing Python file: {inst}"