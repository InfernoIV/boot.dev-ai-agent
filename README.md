# boot.dev-ai-agent
source venv/bin/activate

python3 main.py
python3 tests.py

python3 main.py "What is the meaning of life?"

python3 main.py "what files are in the root?" 
Should return: get_files_info({'directory': '.'})

python3 main.py "what files are in the pkg directory?" 
Should return-> get_files_info({'directory': 'pkg'})

python3 main.py "read the contents of main.py"
##Should return: get_file_content({'file_path': 'main.py'})

python3 main.py "write the text 'hello' to main.txt"
##Should return: write_file({'file_path': 'main.txt', 'content': 'hello'})

python3 main.py "run main.py"
#Should return: run_python_file({'file_path': 'main.py'})

python3 main.py "list the contents of the pkg directory"
#Should return: get_files_info({'directory': 'pkg'})

python3 main.py "explain how the calculator renders the result to the console"