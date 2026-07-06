import sys
import os

while True :
    input_from_user = int(input("Press 1 for addition, 2 for subtraction, 3 for exit : "))

    if input_from_user == 1 :
        print("Doing addition")
        break
    elif input_from_user == 2 :
        print("Doing subtraction")
        break
    elif input_from_user == 3 :
        print("Exiting System.")
        # sys.exit(1)
        os._exit(0)
        os.exit(0)
        # 0 -> successful termination of the program without any errors.
        # 1 -> unsuccessful or abnormal termination

    else :
        print("None of the above, please choose from 1,2 or 3 : ")

print("Out of loop")

