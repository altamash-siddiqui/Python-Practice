"""
Day 32 - Object Oriented Programming
Commit 3: Banking Operations
"""


class BankAccount:

    def __init__(self, account_number, holder_name, balance=0):

        self.account_number = account_number
        self.holder_name = holder_name
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):

        if amount <= 0:
            print("❌ Deposit amount must be positive.")
            return False

        self._balance += amount

        print(
            f"✅ ₹{amount:.2f} deposited successfully."
        )

        return True

    def withdraw(self, amount):

        if amount <= 0:
            print("❌ Withdrawal amount must be positive.")
            return False

        if amount > self._balance:
            print("❌ Insufficient balance.")
            return False

        self._balance -= amount

        print(
            f"✅ ₹{amount:.2f} withdrawn successfully."
        )

        return True

    def show_account(self):

        print("\n" + "=" * 50)
        print("              BANK ACCOUNT")
        print("=" * 50)

        print(f"Account Number : {self.account_number}")
        print(f"Holder Name    : {self.holder_name}")
        print(f"Balance        : ₹{self._balance:.2f}")

        print("=" * 50)


def main():

    account = BankAccount(
        "ACC1001",
        "Altamash",
        5000
    )

    account.show_account()

    account.deposit(2500)

    account.withdraw(1000)

    account.show_account()


if __name__ == "__main__":
    main()