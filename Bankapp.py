
 
import uuid

class Account:
    def __init__(self, acc_no, name, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")
        print(f"{amount} deposited successfully. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrew: {amount}")
            print(f"{amount} withdrawn successfully. New balance: {self.balance}")

    def view_details(self):
        print(f"Account Number: {self.acc_no}\nAccount Holder: {self.name}\nBalance: {self.balance}")

    def print_transactions(self):
        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)


class Bank:
    def __init__(self):
        self.accounts = {}

    def generate_account_number(self):
        # Generate a unique account number using UUID (Universal Unique Identifier)
        return str(uuid.uuid4())[:8]  # Using only the first 8 characters of UUID

    def create_account(self, name, initial_deposit):
        acc_no = self.generate_account_number()
        if acc_no in self.accounts:
            print("Account number already exists!")  # Just in case, though UUIDs should be unique
        else:
            new_account = Account(acc_no, name, initial_deposit)
            self.accounts[acc_no] = new_account
            print(f"Account created successfully for {name} with account number {acc_no}.")

    def view_account_by_accno(self, acc_no):
        if acc_no in self.accounts:
            self.accounts[acc_no].view_details()
        else:
            print("Account not found!")

    def fund_transfer(self, from_acc, to_acc, amount):
        if from_acc not in self.accounts or to_acc not in self.accounts:
            print("One or both account numbers not found!")
        elif self.accounts[from_acc].balance < amount:
            print("Insufficient balance in the sender's account!")
        else:
            self.accounts[from_acc].withdraw(amount)
            self.accounts[to_acc].deposit(amount)
            print(f"Transferred {amount} from account {from_acc} to account {to_acc}.")

    def print_transactions(self, acc_no):
        if acc_no in self.accounts:
            self.accounts[acc_no].print_transactions()
        else:
            print("Account not found!")

    def menu(self):
        while True:
            print("\nBank App")
            print("1. Create Account")
            print("2. View Account Details By Accno")
            print("3. Withdraw")
            print("4. Deposit")
            print("5. Fund transfer")
            print("6. Print Transactions")
            print("7. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                name = input("Enter Account Holder Name: ")
                initial_deposit = float(input("Enter Initial Deposit Amount: "))
                self.create_account(name, initial_deposit)

            elif choice == 2:
                acc_no = input("Enter Account Number: ")
                self.view_account_by_accno(acc_no)

            elif choice == 3:
                acc_no = input("Enter Account Number: ")
                if acc_no in self.accounts:
                    amount = float(input("Enter Amount to Withdraw: "))
                    self.accounts[acc_no].withdraw(amount)
                else:
                    print("Account not found!")

            elif choice == 4:
                acc_no = input("Enter Account Number: ")
                if acc_no in self.accounts:
                    amount = float(input("Enter Amount to Deposit: "))
                    self.accounts[acc_no].deposit(amount)
                else:
                    print("Account not found!")

            elif choice == 5:
                from_acc = input("Enter Sender's Account Number: ")
                to_acc = input("Enter Recipient's Account Number: ")
                amount = float(input("Enter Amount to Transfer: "))
                self.fund_transfer(from_acc, to_acc, amount)

            elif choice == 6:
                acc_no = input("Enter Account Number: ")
                self.print_transactions(acc_no)

            elif choice == 7:
                print("Exiting...")
                break

            else:
                print("Invalid choice! Please try again.")


# Create an instance of the Bank and call the menu
bank = Bank()
bank.menu()