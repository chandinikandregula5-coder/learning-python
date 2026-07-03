class BankAccount:
    def __init__(self):
        self.pin = "1234"
        self.balance = 10000

    def verify_pin(self):
        attempts = 3

        while attempts > 0:
            user_pin = input("Enter Your PIN: ")

            if user_pin == self.pin:
                print("\nLogin Successful!")
                self.menu()
                return
            else:
                attempts -= 1
                if attempts > 0:
                    print(f"Invalid PIN! {attempts} attempt(s) left.")
                else:
                    print("Your account has been blocked after 3 incorrect attempts.")

    def menu(self):
        while True:
            print("\n===== ATM MENU =====")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.deposit()
            elif choice == "2":
                self.withdraw()
            elif choice == "3":
                self.check_balance()
            elif choice == "4":
                print("Thank You!")
                break
            else:
                print("Invalid Choice!")

    def deposit(self):
        try:
            amount = int(input("Enter Deposit Amount: ₹"))

            if amount < 100:
                print("Minimum deposit amount is ₹100.")
            elif amount > 0:
                self.balance += amount
                print("Deposit Successful.")
                print("Current Balance: ₹", self.balance)
            else:
                print("Amount must be greater than 0.")

        except ValueError:
            print("Please enter numbers only.")

    def withdraw(self):
        try:
            amount = int(input("Enter Withdraw Amount: ₹"))

            if amount <= 0:
                print("Invalid Amount!")
            elif amount > self.balance:
                print("Insufficient Balance!")
            elif amount % 100 != 0:
                print("Amount should be a multiple of 100.")
            else:
                self.balance -= amount
                print("Withdrawal Successful.")
                print("Remaining Balance: ₹", self.balance)

        except ValueError:
            print("Please enter numbers only.")

    def check_balance(self):
        print("Available Balance: ₹", self.balance)


atm = BankAccount()
atm.verify_pin()
