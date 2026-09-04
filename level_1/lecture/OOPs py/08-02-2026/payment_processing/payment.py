from customer import Customer
import time
import secrets
import string

class payment():
    def __init__(self,customer):
        self.customer = customer
        self.history = {}

    def add_cash(self,cust_id,method):
        amount = input("enter which method do you preferd:")
        if cust_id in self.customer.cust_data:
            self.Customer.cust_data[cust_id]["balance"]+=amount             
            print(
    f"Hello {self.customer.cust_data[cust_id]['cust_name']} "
    f"your balance is {self.customer.cust_data[cust_id]['balance']}"
)    
    def refund(self,amount,cust_id):
        acc = int(input("Enter account number: "))
        ifsc = input("Enter ifsc code:")
        reason = input("Enter note(why refund): ")
        self.customer.cust_data[cust_id]["balance"]-=amount

    def view_bal(self,cust_id):
        return self.customer.cust_data[cust_id]["balance"]
    
