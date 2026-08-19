"""
Day 32 - Object Oriented Programming
Commit 7: Polymorphism
"""


class BankAccount:

    def __init__(self, account_number, holder_name, balance=0):

        self.account_number = account_number
        self.holder_name = holder_name
        self._balance = balance

    def calculate_benefit(self):

        return 0

    def show_account(self):

        print(
            f"{self.account_number} | "
            f"{self.holder_name} | "
            f"₹{self._balance:.2f}"
        )


class SavingsAccount(BankAccount):

    def __init__(
        self,
        account_number,
        holder_name,
        balance=0
    ):

        super().__init__(
            account_number,
            holder_name,
            balance
        )

        self.interest_rate = 4.0

    def calculate_benefit(self):

        return (
            self._balance *
            self.interest_rate /
            100
        )


class CurrentAccount(BankAccount):

    def __init__(
        self,
        account_number,
        holder_name,
        balance=0
    ):

        super().__init__(
            account_number,
            holder_name,
            balance
        )

        self.cashback_rate = 1.0

    def calculate_benefit(self):

        return (
            self._balance *
            self.cashback_rate /
            100
        )


def show_benefit(account):

    benefit = account.calculate_benefit()

    print(
        f"{account.account_number} → "
        f"Benefit: ₹{benefit:.2f}"
    )


def main():

    accounts = [

        SavingsAccount(
            "SAV1001",
            "Altamash",
            10000
        ),

        CurrentAccount(
            "CUR1001",
            "Altamash",
            20000
        )
    ]

    print("\n" + "=" * 60)
    print("                 ACCOUNT BENEFITS")
    print("=" * 60)

    for account in accounts:

        account.show_account()

        show_benefit(account)

    print("=" * 60)


if __name__ == "__main__":
    main()