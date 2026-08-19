"""
Day 32 - Object Oriented Programming
Commit 4: Custom Exceptions
"""


class InsufficientBalanceError(Exception):
    """Raised when account balance is insufficient."""

    pass


class InvalidAmountError(Exception):
    """Raised when transaction amount is invalid."""

    pass


class BankAccount:

    def __init__(self, account_number, holder_name, balance=0):

        self.account_number = account_number
        self.holder_name = holder_name
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):

        if amount <= 0:
            raise InvalidAmountError(
                "Deposit amount must be greater than zero."
            )

        self._balance += amount

    def withdraw(self, amount):

        if amount <= 0:
            raise InvalidAmountError(
                "Withdrawal amount must be greater than zero."
            )

        if amount > self._balance:
            raise InsufficientBalanceError(
                "Insufficient balance for this withdrawal."
            )

        self._balance -= amount

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

    try:

        account.deposit(2000)

        account.withdraw(1000)

        account.withdraw(10000)

    except InsufficientBalanceError as error:

        print(f"❌ Transaction failed: {error}")

    except InvalidAmountError as error:

        print(f"❌ Invalid transaction: {error}")

    account.show_account()


if __name__ == "__main__":
    main()