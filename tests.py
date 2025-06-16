#Create a new tests.py file in the root of your project. When executed directly, it should:
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file
from main import main

def test_get_files_info():
    #Run get_files_info("calculator", ".") and print the result to the console.
    print(get_files_info("calculator", "."))
    print("\r\n")

    #Run get_files_info("calculator", "pkg") and print the result to the console.
    print(get_files_info("calculator", "pkg"))
    print("\r\n")

    #Run get_files_info("calculator", "/bin") and print the result to the console (this should return an error string)
    print(get_files_info("calculator", "/bin"))
    print("\r\n")

    #Run get_files_info("calculator", "../") and print the result to the console (this should return an error string)
    print(get_files_info("calculator", "../"))
    print("\r\n")


def test_get_file_content():

    print(get_file_content("calculator", "lorem.txt")) #Ensure that it truncates properly.
    print("\r\n")

    print(get_file_content("calculator", "main.py"))
    print("\r\n")

    print(get_file_content("calculator", "pkg/calculator.py"))
    print("\r\n")

    print(get_file_content("calculator", "/bin/cat")) #(this should return an error string)
    print("\r\n")


def test_write_file():
    #28 characters written
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    print("\r\n")

    #26 characters written
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print("\r\n")

    #Error:
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
    print("\r\n")


def test_run_python_file():
    print(run_python_file("calculator", "main.py"))
    print("\r\n")

    print(run_python_file("calculator", "tests.py"))
    print("\r\n")

    #(this should return an error)
    print(run_python_file("calculator", "../main.py"))
    print("\r\n")

    #(this should return an error)
    print(run_python_file("calculator", "nonexistent.py"))
    print("\r\n")

  
#exectue desired test function
#test_get_files_info()
#test_get_file_content()
#test_write_file()
#test_run_python_file()