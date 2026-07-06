# # import os
# # print(os.getcwd())

# try:
#     with open("..\\temp\\temp_2.txt","r") as f:
#         content = f.read()
#         print(content)
# except:
#     print("file not found")

# # =====================================================
# value_1 = input("Enter value for addition")

# def add(val_1,val_2):
#     try:
#         return val_1 + val_2
#     except:
#         print("error in calculation, handling it using try and except")
#         return val_1 + float(val_2)
    
# calc = add(100,value_1)

# print(calc)
# print("hello")

import os

print("Try and except block is started.")
try:
    num= 0
    folder = "..\\temp"
    file = "temp_1_copy"
    print(os.path.join(folder,file))
    with open("..\\temp\\temp_1_copyl.txt","r") as f:
        cont = f.read()
        print(cont)

    cal = 100/num

except FileNotFoundError:
    print("File not found,Please check correct file name or path")
    print("Current location is : ", os.getcwd())
    print("Files present in current directory : ", os.listdir(os.path.join(os.getcwd(),folder)))
    print("File name selected : ", "temp/temp_3.txt")
except TypeError:
    print("Issue with multiple type operation.")
except Exception as e:
    print("Caught in parent exception", e)
else : 
    print("try block successfully execute.")
print("Try except block completed.")

