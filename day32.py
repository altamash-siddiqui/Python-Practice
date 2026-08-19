"""
Day 32 - Object Oriented Programming
Commit 1: Account Model

A real-world banking system using Python classes.
"""


class BankAccount:
    """Represents a basic bank account."""

    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def show_account(self):
        """Display account information."""

        print("\n" + "=" * 50)
        print("              BANK ACCOUNT")
        print("=" * 50)

        print(f"Account Number : {self.account_number}")
        print(f"Holder Name    : {self.holder_name}")
        print(f"Balance        : ₹{self.balance:.2f}")

        print("=" * 50)


def main():
    account = BankAccount(
        account_number="ACC1001",
        holder_name="Altamash",
        balance=5000
    )

    account.show_account()


if __name__ == "__main__":
    main()