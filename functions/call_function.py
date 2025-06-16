from google import genai
from google.genai import types # type: ignore
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

constrained_folder = "./calculator"

string_to_function = {
    "get_files_info": get_files_info,
    "get_file_content": get_file_content,
    "write_file": write_file,
    "run_python_file": run_python_file,
}


def call_function(function_call_part: types.FunctionCall, verbose: bool = False):
    #if we want more information
    if verbose:
        #print more information
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        #print basic information
        #print(f" - Calling function: {function_call_part.name}")
        pass
    
    #if requested function does not exist 
    if function_call_part.name not in string_to_function:
        #stop
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Unknown function: {function_call_part.name}"},
                )
            ],
        )

    #get the function
    function = string_to_function[function_call_part.name]
    #set the base directory
    
    #save the arguments
    arguments = function_call_part.args
    #be sure to manually add the "working_directory" argument to the dictionary of keyword arguments, because the LLM doesn't control that one. The working directory should be ./calculator.
    arguments["working_directory"] = constrained_folder #"./calculator"
    #The syntax to pass a dictionary into a function using keyword arguments is some_function(**some_args)
    result = function(**arguments)

    #return the result
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call_part.name,
                response={"result": result},
            )
        ],
    )
