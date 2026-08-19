"""
Day 32 - Object Oriented Programming
Commit 2: Encapsulation

Demonstrates controlled access to account data.
"""


class BankAccount:
    """Represents a bank account with encapsulated balance."""

    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name

        # Protected-style internal balance
        self._balance = balance

    def get_balance(self):
        """Return the current account balance."""

        return self._balance

    def show_account(self):
        """Display account information."""

        print("\n" + "=" * 50)
        print("              BANK ACCOUNT")
        print("=" * 50)

        print(f"Account Number : {self.account_number}")
        print(f"Holder Name    : {self.holder_name}")
        print(f"Balance        : ₹{self.get_balance():.2f}")

        print("=" * 50)


def main():

    account = BankAccount(
        account_number="ACC1001",
        holder_name="Altamash",
        balance=5000
    )

    account.show_account()

    print(
        f"\nCurrent Balance: ₹{account.get_balance():.2f}"
    )


if __name__ == "__main__":
    main()