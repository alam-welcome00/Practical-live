from customer import Customer
import time
import secrets
import string


class Transaction:
    def __init__(self, customer):
        self.customer = customer
        self.history = {}

    def transaction_id_generate(self):
        # Bug fix: was `t1 + trans_id_1` where t1 is a float and trans_id_1
        # is a string -> TypeError. Cast t1 to int/str first.
        t1 = int(time.time())
        pool = string.ascii_lowercase + string.digits
        trans_id_1 = "".join(secrets.choice(pool) for _ in range(10))
        return f"{t1}{trans_id_1}"

    def record_transaction(self, cust_id, amount, method, transaction_type):
        trans_id = self.transaction_id_generate()
        # Bug fix: was `self.history = {trans_id: {...}}` which OVERWRITES
        # all previous transactions. Using [trans_id] = {...} appends instead.
        self.history[trans_id] = {
            "cust_id": cust_id,
            "amount": amount,
            "method": method,
            "transaction_type": transaction_type,  # fixed typo "ttransaction_type"
            "time": time.time(),
        }
        return trans_id

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

    def transaction_by_cust_id(self, cust_id):
        found = False

        for trans_id, detail in self.history.items():
            if detail["cust_id"] == cust_id:
                found = True
                # Bug fix: these prints were outside the if block before,
                # so every transaction printed regardless of match.
                print("-" * 30)
                print("Transaction ID :", trans_id)
                for key, value in detail.items():
                    print(f"{key} : {value}")

        if not found:
            print("No transaction found.")

    def total_transaction(self):
        # Bug fix: was missing a closing parenthesis -> SyntaxError,
        # the whole file couldn't even be imported.
        print("Total Transactions :", len(self.history))
