import string
import secrets
import time


class Customer:
    def __init__(self):
        self.cust_data = {}

    def add_user(self, type_of_user, type_of_acc, balance):
        cust_name = input("Enter your valid name: ")

        while True:
            try:
                cust_age = int(input("Enter your age as per govt ID: "))
                break
            except ValueError:
                print("Please enter a valid number for age.")

        while True:
            try:
                number = int(input("Enter your phone number: "))
                break
            except ValueError:
                print("Please enter a valid phone number.")

        cust_id_first = "".join(cust_name.split())[:4].upper()
        pool = string.ascii_uppercase + string.digits
        cust_id_second = "".join(secrets.choice(pool) for _ in range(10))
        cust_id = cust_id_first + cust_id_second

        # Bug fix: was `self.cust_data = {...}` which OVERWRITES the whole
        # dict on every call. Using [cust_id] = {...} adds/updates just
        # this one entry instead of wiping everyone else out.
        self.cust_data[cust_id] = {
            "cust_name": cust_name,
            "cust_age": cust_age,
            "cust_contact": number,
            "user_type": type_of_user,   # now actually stored
            "acc_type": type_of_acc,     # now actually stored
            "create_At": time.time(),
            "balance": float(balance),
        }

        print(f"\nCustomer registered successfully! Your customer ID is: {cust_id}\n")
        return cust_id  # caller can now capture this instead of guessing

    def register_cust(self):
        if not self.cust_data:
            print("No customers registered yet.")
            return
        for cust_id, details in self.cust_data.items():
            print(f"{cust_id}: {details}")
