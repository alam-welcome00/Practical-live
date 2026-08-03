from customer import Customer
import time
import secrets
import string

class transaction():
    def __init__(self,customer):
        self.customer = customer
        self.history = {}

    def transaction_id_generate(self):
        t1 = time.time()
        pool = string.ascii_lowercase +string.digits
        trans_id_1 = "".join(secrets.choice(pool) for _ in range(10))
        self.trans_id = t1+trans_id_1 
        
    def record_transaction(self,cust_id, amount, method, transaction_type,trans_id):
        self.history = {trans_id: {
                "cust_id":cust_id,
                "amount":amount,
                "method":method,
                "ttransaction_type":transaction_type

            }
        }

    def view_all_transactions(self):
        if not self.history:
            print("No transactions found.")
            return

        for trans_id, details in self.history.items():
            print("-" * 40)
            print(f"Transaction ID : {trans_id}")

            for key, value in details.items():
                print(f"{key:<10} : {value}")

            print("-" * 40)

    def transaction_by_cust_id(self,cust_id):
        found  = False

        for trans_id,detail in self.history.items():
            if detail["cust_id"]==cust_id:
                found= True

            print("-"*30)
            print("Transaction ID :", trans_id)

            for key, value in detail.items():
                print(f"{key} : {value}")

        if not found:
            print("No transaction found.")
            

    def total_transaction(self):
        print("Total Transactions :", len(self.history))