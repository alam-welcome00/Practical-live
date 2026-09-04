from customer import Customer


class Payment:
    def __init__(self, customer):
        self.customer = customer
        self.history = {}

    def add_cash(self, cust_id, amount, method):
        if cust_id not in self.customer.cust_data:
            print("Customer not found.")
            return False

        # Bug fix: was self.Customer (capital C, doesn't exist) -> AttributeError.
        # Also: amount is now a real parameter instead of an unconverted
        # input() string mistakenly stored in a variable called "amount".
        self.customer.cust_data[cust_id]["balance"] += amount
        print(
            f"Hello {self.customer.cust_data[cust_id]['cust_name']}, "
            f"your balance is {self.customer.cust_data[cust_id]['balance']}"
        )
        return True

    def refund(self, amount, cust_id):
        if cust_id not in self.customer.cust_data:
            print("Customer not found.")
            return False

        if self.customer.cust_data[cust_id]["balance"] < amount:
            print("Insufficient balance for refund.")
            return False

        acc = input("Enter account number: ")
        ifsc = input("Enter IFSC code: ")
        reason = input("Enter note (why refund): ")

        self.customer.cust_data[cust_id]["balance"] -= amount
        print(f"Refund of {amount} processed to account {acc} ({ifsc}). Reason: {reason}")
        return True

    def view_bal(self, cust_id):
        if cust_id not in self.customer.cust_data:
            print("Customer not found.")
            return None
        return self.customer.cust_data[cust_id]["balance"]
