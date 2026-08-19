"""
Day 32 - Object Oriented Programming
Commit 5: Transaction History
"""


class InsufficientBalanceError(Exception):
    pass


class InvalidAmountError(Exception):
    pass


class BankAccount:

    def __init__(self, account_number, holder_name, balance=0):

        self.account_number = account_number
        self.holder_name = holder_name
        self._balance = balance
        self._transactions = []

        if balance > 0:

            self._transactions.append({
                "type": "Opening Balance",
                "amount": balance,
                "balance": balance
            })

    def get_balance(self):
        return self._balance

    def deposit(self, amount):

        if amount <= 0:
            raise InvalidAmountError(
                "Deposit amount must be greater than zero."
            )

        self._balance += amount

        self._transactions.append({
            "type": "Deposit",
            "amount": amount,
            "balance": self._balance
        })

    def withdraw(self, amount):

        if amount <= 0:
            raise InvalidAmountError(
                "Withdrawal amount must be greater than zero."
            )

        if amount > self._balance:
            raise InsufficientBalanceError(
                "Insufficient balance."
            )

        self._balance -= amount

        self._transactions.append({
            "type": "Withdrawal",
            "amount": amount,
            "balance": self._balance
        })

    def show_transactions(self):

        print("\n" + "=" * 65)
        print("                  TRANSACTION HISTORY")
        print("=" * 65)

        if not self._transactions:

            print("No transactions available.")

            return

        for number, transaction in enumerate(
            self._transactions,
            start=1
        ):

            print(
                f"{number}. "
                f"{transaction['type']:<18}"
                f"₹{transaction['amount']:>10.2f}"
                f" | Balance: ₹{transaction['balance']:.2f}"
            )

        print("=" * 65)

    def show_account(self):

        print("\n" + "=" * 50)

        print(f"Account : {self.account_number}")
        print(f"Holder  : {self.holder_name}")
        print(f"Balance : ₹{self._balance:.2f}")

        print("=" * 50)


def main():

    account = BankAccount(
        "ACC1001",
        "Altamash",
        5000
    )

    try:

        account.deposit(2000)
        account.withdraw(1200)
        account.deposit(3500)
        account.withdraw(500)

    except (
        InsufficientBalanceError,
        InvalidAmountError
    ) as error:

        print(f"❌ Transaction failed: {error}")

    account.show_account()

    account.show_transactions()


if __name__ == "__main__":
    main()