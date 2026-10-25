class BankAccount:
    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number

        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")

        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self.balance += amount
        print(f"Deposited: Rs. {amount:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        if amount > self.balance:
            raise ValueError("Insufficient balance.")

        self.balance -= amount
        print(f"Withdrawn: Rs. {amount:.2f}")

    def display_balance(self):
        print(f"Account holder: {self.account_holder}")
        print(f"Account number: {self.account_number}")
        print(f"Current balance: Rs. {self.balance:.2f}")


def main():
    account = BankAccount("Raga", "ACC1001", 5000)

    account.display_balance()

    account.deposit(1500)
    account.withdraw(2000)

    print("\nAfter transactions:")
    account.display_balance()


if __name__ == "__main__":
    main()
