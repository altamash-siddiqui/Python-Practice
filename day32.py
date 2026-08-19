"""
Day 32 - Object Oriented Programming
Commit 6: Account Inheritance
"""


class BankAccount:

    def __init__(self, account_number, holder_name, balance=0):

        self.account_number = account_number
        self.holder_name = holder_name
        self._balance = balance

    def deposit(self, amount):

        if amount <= 0:
            raise ValueError(
                "Deposit amount must be positive."
            )

        self._balance += amount

    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError(
                "Withdrawal amount must be positive."
            )

        if amount > self._balance:
            raise ValueError(
                "Insufficient balance."
            )

        self._balance -= amount

    def show_account(self):

        print("\n" + "=" * 50)

        print(f"Account : {self.account_number}")
        print(f"Holder  : {self.holder_name}")
        print(f"Balance : ₹{self._balance:.2f}")

        print("=" * 50)


class SavingsAccount(BankAccount):

    def __init__(
        self,
        account_number,
        holder_name,
        balance=0,
        interest_rate=4.0
    ):

        super().__init__(
            account_number,
            holder_name,
            balance
        )

        self.interest_rate = interest_rate

    def calculate_interest(self):

        interest = (
            self._balance *
            self.interest_rate /
            100
        )

        return interest


class CurrentAccount(BankAccount):

    def __init__(
        self,
        account_number,
        holder_name,
        balance=0,
        minimum_balance=1000
    ):

        super().__init__(
            account_number,
            holder_name,
            balance
        )

        self.minimum_balance = minimum_balance


def main():

    savings = SavingsAccount(
        "SAV1001",
        "Altamash",
        10000
    )

    current = CurrentAccount(
        "CUR1001",
        "Altamash",
        15000
    )

    savings.show_account()

    print(
        f"Annual Interest: "
        f"₹{savings.calculate_interest():.2f}"
    )

    current.show_account()


if __name__ == "__main__":
    main()