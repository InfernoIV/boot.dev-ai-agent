#Create a new tests.py file in the root of your project. When executed directly, it should:
from functions.get_files_info import get_files_info

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
