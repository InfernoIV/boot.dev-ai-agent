import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


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
        #print(f"Input: '{sys.argv[1]}'")
        #post the question
        handle_assignment(sys.argv[1],verbose)
        pass
    return


def handle_assignment(user_prompt, verbose):
    #constant
    model = "gemini-2.0-flash-001"

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    
    if verbose:
        print(f"User prompt: {user_prompt}")

    #post message and get response
    response = client.models.generate_content(
        model=model,#'gemini-2.0-flash-001', 
        contents=messages#"Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    )

    #print response
    print(response.text)
    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    #
    return

#exectue main function
main()