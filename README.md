# boot.dev-ai-agent
source venv/bin/activate

python3 main.py

python3 main.py "What is the meaning of life?"

python3 main.py "what files are in the root?" 
Should return: get_files_info({'directory': '.'})

python3 main.py "what files are in the pkg directory?" 
Should return-> get_files_info({'directory': 'pkg'})