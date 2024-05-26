#student number: 0223011
#Department: Electronics and Communication Engineering
# Assignment 2
#reference 1 :https://www.youtube.com/watch?v=julcNz6rWVc 
#references 2:https://www.youtube.com/watch?v=cthx6jeLtW8 
#referenc 3:https://www.youtube.com/watch?v=y_kk7NLGcas 


import random  # Step 1: Importing the random module for generating random account numbers and passwords
import os  # Step 2: Importing the os module for file operations

# Step 3: Define the base class for any type of account
class Account:
    def __init__(self, account_number, password, account_type, balance=0.0):
        # Step 3.1: Initialize account with number, password, type, and balance
        self.account_number = account_number
        self.password = password
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        # Step 3.2: Method to deposit amount into the account
        self.balance += amount  # Step 3.2.1: Increase balance by the deposit amount
        print(f"Deposited {amount}. New balance: {self.balance}")  # Step 3.2.2: Print the new balance

    def withdraw(self, amount):
        # Step 3.3: Method to withdraw amount from the account
        if self.balance >= amount:  # Step 3.3.1: Check if sufficient balance is available
            self.balance -= amount  # Step 3.3.2: Decrease balance by the withdrawal amount
            print(f"Withdrew {amount}. New balance: {self.balance}")  # Step 3.3.3: Print the new balance
        else:
            print("Insufficient funds.")  # Step 3.3.4: Print error message if balance is insufficient

    def __str__(self):
        # Step 3.4: String representation of the account object
        return f"Account Number: {self.account_number}, Balance: {self.balance}, Type: {self.account_type}"

# Step 4: Define subclass for personal accounts
class PersonalAccount(Account):
    def __init__(self, account_number, password, balance=0.0):
        # Step 4.1: Initialize personal account using the parent class constructor
        super().__init__(account_number, password, "Personal", balance)

# Step 5: Define subclass for business accounts
class BusinessAccount(Account):
    def __init__(self, account_number, password, balance=0.0):
        # Step 5.1: Initialize business account using the parent class constructor
        super().__init__(account_number, password, "Business", balance)

# Step 6: Define the class to manage all bank operations
class Bank:
    def __init__(self, accounts_file="accounts.txt"):
        # Step 6.1: Initialize bank with accounts file
        self.accounts_file = accounts_file  # Step 6.1.1: Set the file to store account data
        self.load_accounts()  # Step 6.1.2: Load existing accounts from the file

    def load_accounts(self):
        # Step 6.2: Method to load accounts from file
        self.accounts = {}  # Step 6.2.1: Initialize an empty dictionary to store accounts
        if os.path.exists(self.accounts_file):  # Step 6.2.2: Check if accounts file exists
            with open(self.accounts_file, "r") as file:  # Step 6.2.3: Open file in read mode
                for line in file:  # Step 6.2.4: Read each line from the file
                    account_number, password, account_type, balance = line.strip().split(",")  # Step 6.2.5: Parse account details
                    balance = float(balance)  # Step 6.2.6: Convert balance to float
                    if account_type == "Personal":  # Step 6.2.7: Check account type
                        account = PersonalAccount(account_number, password, balance)  # Step 6.2.8: Create PersonalAccount object
                    elif account_type == "Business":  # Step 6.2.9: Check account type
                        account = BusinessAccount(account_number, password, balance)  # Step 6.2.10: Create BusinessAccount object
                    self.accounts[account_number] = account  # Step 6.2.11: Add account to dictionary

    def save_accounts(self):
        # Step 6.3: Method to save accounts to file
        with open(self.accounts_file, "w") as file:  # Step 6.3.1: Open file in write mode
            for account in self.accounts.values():  # Step 6.3.2: Iterate through each account
                file.write(f"{account.account_number},{account.password},{account.account_type},{account.balance}\n")  # Step 6.3.3: Write account details to file

    def create_account(self, account_type):
        # Step 6.4: Method to create a new account
        account_number = str(random.randint(10000, 99999))  # Step 6.4.1: Generate a random account number
        password = str(random.randint(1000, 9999))  # Step 6.4.2: Generate a random password
        if account_type == "Personal":  # Step 6.4.3: Check account type
            account = PersonalAccount(account_number, password)  # Step 6.4.4: Create PersonalAccount object
        elif account_type == "Business":  # Step 6.4.5: Check account type
            account = BusinessAccount(account_number, password)  # Step 6.4.6: Create BusinessAccount object
        self.accounts[account_number] = account  # Step 6.4.7: Add new account to dictionary
        self.save_accounts()  # Step 6.4.8: Save accounts to file
        print(f"Account created successfully. Account Number: {account_number}, Password: {password}")  # Step 6.4.9: Print success message

    def login(self, account_number, password):
        # Step 6.5: Method to login to an account
        account = self.accounts.get(account_number)  # Step 6.5.1: Retrieve account by account number
        if account and account.password == password:  # Step 6.5.2: Check if account exists and password matches
            return account  # Step 6.5.3: Return the account object if login is successful
        else:
            print("Invalid account number or password.")  # Step 6.5.4: Print error message if login fails
            return None  # Step 6.5.5: Return None if login fails

    def delete_account(self, account_number):
        # Step 6.6: Method to delete an account
        if account_number in self.accounts:  # Step 6.6.1: Check if account exists
            del self.accounts[account_number]  # Step 6.6.2: Delete account from dictionary
            self.save_accounts()  # Step 6.6.3: Save changes to file
            print(f"Account {account_number} deleted successfully.")  # Step 6.6.4: Print success message
        else:
            print("Account does not exist.")  # Step 6.6.5: Print error message if account does not exist

    def transfer_money(self, from_account, to_account_number, amount):
        # Step 6.7: Method to transfer money between accounts
        if from_account.balance < amount:  # Step 6.7.1: Check if sender has sufficient balance
            print("Insufficient funds.")  # Step 6.7.2: Print error message if insufficient balance
            return  # Step 6.7.3: Exit the method
        to_account = self.accounts.get(to_account_number)  # Step 6.7.4: Retrieve recipient account by account number
        if to_account:  # Step 6.7.5: Check if recipient account exists
            from_account.withdraw(amount)  # Step 6.7.6: Withdraw amount from sender's account
            to_account.deposit(amount)  # Step 6.7.7: Deposit amount to recipient's account
            self.save_accounts()  # Step 6.7.8: Save changes to file
            print(f"Transferred {amount} from {from_account.account_number} to {to_account_number}.")  # Step 6.7.9: Print success message
        else:
            print("Receiving account does not exist.")  # Step 6.7.10: Print error message if recipient account does not exist

# Step 7: Define the main function to run the banking application
def main():
    bank = Bank()  # Step 7.1: Create an instance of the Bank class
    while True:
        # Step 7.2: Display main menu
        print("\nWelcome to the Banking Application")
        print("1. Open an Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")  # Step 7.3: Get user's choice

        if choice == '1':
            # Step 7.4: Option to open a new account
            account_type = input("Enter account type (Personal/Business): ")  # Step 7.4.1: Get account type from user
            bank.create_account(account_type)  # Step 7.4.2: Call create_account method

        elif choice == '2':
            # Step 7.5: Option to login to an account
            account_number = input("Enter your account number: ")  # Step 7.5.1: Get account number from user
            password = input("Enter your password: ")  # Step 7.5.2: Get password from user
            account = bank.login(account_number, password)  # Step 7.5.3: Call login method
            if account:
                # Step 7.5.4: If login is successful, display account menu
                while True:
                    print("\n1. Check Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Fund Transfer")
                    print("5. Delete Account")
                    print("6. Logout")
                    user_choice = input("Choose an option: ")  # Step 7.5.5: Get user's choice

                    if user_choice == '1':
                        # Step 7.5.6: Option to check balance
                        print(f"Balance: {account.balance}")  # Step 7.5.6.1: Print account balance

                    elif user_choice == '2':
                        # Step 7.5.7: Option to deposit money
                        amount = float(input("Enter amount to deposit: "))  # Step 7.5.7.1: Get deposit amount from user
                        account.deposit(amount)  # Step 7.5.7.2: Call deposit method
                        bank.save_accounts()  # Step 7.5.7.3: Save changes to file

                    elif user_choice == '3':
                        # Step 7.5.8: Option to withdraw money
                        amount = float(input("Enter amount to withdraw: "))  # Step 7.5.8.1: Get withdrawal amount from user
                        account.withdraw(amount)  # Step 7.5.8.2: Call withdraw method
                        bank.save_accounts()  # Step 7.5.8.3: Save changes to file

                    elif user_choice == '4':
                        # Step 7.5.9: Option to transfer money
                        to_account_number = input("Enter the recipient account number: ")  # Step 7.5.9.1: Get recipient account number
                        amount = float(input("Enter amount to transfer: "))  # Step 7.5.9.2: Get transfer amount
                        bank.transfer_money(account, to_account_number, amount)  # Step 7.5.9.3: Call transfer_money method

                    elif user_choice == '5':
                        # Step 7.5.10: Option to delete account
                        bank.delete_account(account.account_number)  # Step 7.5.10.1: Call delete_account method
                        break  # Step 7.5.10.2: Exit to main menu

                    elif user_choice == '6':
                        # Step 7.5.11: Option to logout
                        break  # Step 7.5.11.1: Exit to main menu

                    else:
                        print("Invalid choice. Please try again.")  # Step 7.5.12: Print error message for invalid choice

        elif choice == '3':
            # Step 7.6: Option to exit the application
            print("Thank you for using the Banking Application. Goodbye!")  # Step 7.6.1: Print exit message
            break  # Step 7.6.2: Exit the main loop

        else:
            print("Invalid choice. Please try again.")  # Step 7.7: Print error message for invalid choice

if __name__ == "__main__":
    main()  # Step 8: Run the main function to start the application

