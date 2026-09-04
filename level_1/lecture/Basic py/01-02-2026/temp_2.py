import os

print("Try except block started.")
try:
    
    folder_name = "temp"
    file_name = "temp_2.txt"
    num = 1

    file_path = os.path.join(folder_name,file_name)
    with open(file_path, "r+") as f:
        contents = f.read()
        print(contents)

    cal = 100 / num # infinity, not divisible

except FileNotFoundError:
    print("File not found,Please check correct file name or path")
    print("Current location is : ", os.getcwd())
    print("Files present in current directory : ", os.listdir(os.path.join(os.getcwd(),folder_name)))
    print("File name selected : ", "temp/temp_3.txt")
except TypeError:
    print("Issue with multiple type operation.")
except Exception as e:
    print("Caught in parent exception", e)
else : 
    print("try block successfully execute.")
print("Try except block completed.")


# folder_name = "temp"
# file_name = "temp_3.txt"
# file_path = os.path.join(folder_name,file_name)
# with open(file_path, "r+") as f:
#     contents = f.read()
#     print(contents)

