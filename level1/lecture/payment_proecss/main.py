from customer import Customer
from payment import Payment
from transaction import Transaction


def main():
    # One shared Customer store, passed into both Payment and Transaction
    # so they all read/write the same data instead of separate copies.
    customer = Customer()
    payment = Payment(customer)
    transaction = Transaction(customer)

    menu = """
==== Simple Payment Processing System ====
1. Register new customer
2. Add cash to wallet
3. Refund
4. View balance
5. View all customers
6. View all transactions
7. View transactions by customer ID
8. Exit
"""

    while True:
        print(menu)
        choice = input("Choose an option: ").strip()

        if choice == "1":
            type_of_user = input("Enter user type (e.g. regular/premium): ")
            type_of_acc = input("Enter account type (e.g. savings/wallet): ")
            starting_balance = input("Enter starting balance (leave blank for 0): ")
            starting_balance = float(starting_balance) if starting_balance else 0.0
            customer.add_user(type_of_user, type_of_acc, starting_balance)

        elif choice == "2":
            cust_id = input("Enter customer ID: ").strip()
            method = input("Enter payment method (UPI/Card/Cash): ").strip()
            try:
                amount = float(input("Enter amount to add: "))
            except ValueError:
                print("Invalid amount.")
                continue

            if payment.add_cash(cust_id, amount, method):
                transaction.record_transaction(cust_id, amount, method, "credit")

        elif choice == "3":
            cust_id = input("Enter customer ID: ").strip()
            try:
                amount = float(input("Enter refund amount: "))
            except ValueError:
                print("Invalid amount.")
                continue

            if payment.refund(amount, cust_id):
                transaction.record_transaction(cust_id, amount, "refund", "debit")

        elif choice == "4":
            cust_id = input("Enter customer ID: ").strip()
            bal = payment.view_bal(cust_id)
            if bal is not None:
                print(f"Balance: {bal}")

        elif choice == "5":
            customer.register_cust()

        elif choice == "6":
            transaction.view_all_transactions()

        elif choice == "7":
            cust_id = input("Enter customer ID: ").strip()
            transaction.transaction_by_cust_id(cust_id)

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()
