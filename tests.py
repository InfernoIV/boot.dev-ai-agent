#Create a new tests.py file in the root of your project. When executed directly, it should:
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

#Update your tests.py file. Remove all the calls to get_files_info, and instead test get_file_content("calculator", "lorem.txt"). Ensure that it truncates properly.
#print(get_file_content("calculator", "lorem.txt")) #Ensure that it truncates properly.
#print("\r\n")

print(get_file_content("calculator", "main.py"))
print("\r\n")

print(get_file_content("calculator", "pkg/calculator.py"))
print("\r\n")

print(get_file_content("calculator", "/bin/cat")) #(this should return an error string)
print("\r\n")




#Run get_files_info("calculator", ".") and print the result to the console.
#print(get_files_info("calculator", "."))
#print("\r\n")

#Run get_files_info("calculator", "pkg") and print the result to the console.
#print(get_files_info("calculator", "pkg"))
#print("\r\n")

#Run get_files_info("calculator", "/bin") and print the result to the console (this should return an error string)
#print(get_files_info("calculator", "/bin"))
#print("\r\n")

#Run get_files_info("calculator", "../") and print the result to the console (this should return an error string)
#print(get_files_info("calculator", "../"))
#print("\r\n")