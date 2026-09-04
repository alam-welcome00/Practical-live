
try:
    with open("temp/temp_3.txt", "r+") as f:
        contents = f.read()
        print(contents)
except :
    print("File not found")

# with open("temp/temp_3.txt", "r+") as f: # FileNotFoundError
#     contents = f.read()
#     print(contents)


#############################################################

value_1 = input("Enter a number to add : ")

def add(val_1, val_2):
    try : 
        return val_1 + val_2
    except :
        print("Error in calculation, handling it using type casting.")
        return val_1 + float(val_2)
    # return val_1 + val_2 # TypeError

calc = add(100, value_1)
print(calc)
print("hello world")

# handle error such that other things should work
# handle error such that it will not break the system

# exception handling
