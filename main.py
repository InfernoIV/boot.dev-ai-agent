import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types # type: ignore
from schemas import available_functions
from functions.call_function import call_function 

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
max_iterations = 30


def main():
    #print(f"Args: '{sys.argv[1:]}'")
    if len(sys.argv) < 2:
        sys.exit("No arguments!")
    elif len(sys.argv) > 3: 
        sys.exit(f"Too many arguments! {sys.argv[1:]}")
    else:  
        optional_argument = ""     
        if len(sys.argv) > 2:
            optional_argument = sys.argv[2]
        verbose = optional_argument.lower() == "--verbose"
        #post the question
        generate_content(sys.argv[1], verbose)
        pass
    return


def generate_content(user_prompt: str, verbose: bool):
    #constants
    model = "gemini-2.0-flash-001"
    system_prompt = system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    
    if verbose:
        print(f"User prompt: {user_prompt}")

    #starting value
    iteration = 0
    #save last response
    last_response = ""

    #run forever (breaks from inside the loop)
    while iteration < max_iterations: 
        #new iteration
        iteration += 1

        #debug
        #print(f"iteration: {iteration}")
        #print(f"Messages: \"{messages}\"")

        #post message and get response
        response = client.models.generate_content(
            model=model,#'gemini-2.0-flash-001', 
            contents=messages,#"Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
            config=types.GenerateContentConfig(
                tools=[available_functions], system_instruction=system_prompt)
        )
        
        #save the last response
        last_response = response.text
        
        #process message
        for candidate in response.candidates:
            #add message to the list
            messages.append(candidate.content)

        if response.function_calls != None:
            #for each request
            for function_call in response.function_calls:
                #call the function and print the result
                result = call_function(function_call, verbose)
                #print(f"result: \"{result}\"")
                try:
                    #get the response (will trigger exception if not present)
                    function_response = result.parts[0].function_response.response
                    #print if needed
                    if verbose:
                        print(f"-> {function_response}")
                    #add message to list
                    messages.append(types.Content(role="user", parts=result.parts))
                    

                except Exception as inst:
                    print(f"*****Error: {inst}")
                    print(f"*****result: {result}")
                    return        

        #no function call, done?
        else:
            #print(f"*****No more function calls! ({response})")
            #stop
            break

    #print the last message
    print(f"Result: \"{last_response}\"")

    #print token information if needed
    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    
    return
    

#fix the logging
import logging

class _NoFunctionCallWarning(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        message = record.getMessage()
        if "there are non-text parts in the response:" in message:
            return False
        else:
            return True

logging.getLogger("google_genai.types").addFilter(_NoFunctionCallWarning())

#exectue main function
main()