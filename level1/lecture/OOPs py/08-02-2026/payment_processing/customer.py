import string
import secrets
import time

class Customer:
    def __init__(self):
        self.cust_data = {}

    def add_user(self,type_of_user,type_of_acc,balance):
        cust_name = input("Enter your valid name: ")
        cust_age = int(input("Enter your age as per govnt ID: "))
        number = int(input("Enter your phone number: "))
        cust_id_first = "".join(cust_name.split())[:4].upper()
        pool = string.ascii_uppercase + string.digits
        cust_id_second = "".join(secrets.choice(pool) for _ in range(10))
        cust_id = cust_id_first + cust_id_second
        balance = balance
        creation_time = time.time()

        self.cust_data ={cust_id:{"cust_name":cust_name,
                                    "cust_age":cust_age,
                                    "cust_contact":number,
                                    "create_At":creation_time,
                                    "balance":balance}
                                    }
    def register_cust(self):
        for a,b in self.cust_data.items():
            print(f"{a}:{b}")
        

