import os, sys
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def main():
    if len(sys.argv) < 2:
        sys.exit("No arguments!")
    elif len(sys.argv) > 2: 
        sys.exit(f"Too many arguments! {sys.argv[1:]}")
    else:
        #print(f"Input: '{sys.argv[1]}'")
        #post the question
        handle_assignment(sys.argv[1])
        pass
    return


def handle_assignment(command):
    #constant
    model = "gemini-2.0-flash-001"
    #post message and get response
    response = client.models.generate_content(
        model=model,#'gemini-2.0-flash-001', 
        contents=command#"Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    )
    #print response
    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    #
    return

#exectue main function
main()