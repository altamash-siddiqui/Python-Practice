"""
Day 32 - Python OOP
Commit 8: Complete Banking System

Concepts:
- Classes & Objects
- Encapsulation
- Inheritance
- Polymorphism
- Custom Exceptions
- Transaction History
- Class Methods
"""


class InsufficientBalanceError(Exception):
    """Raised when withdrawal exceeds available balance."""

    pass


class InvalidAmountError(Exception):
    """Raised when transaction amount is invalid."""

    pass


class BankAccount:

    bank_name = "Python National Bank"

    def __init__(
        self,
        account_number,
        holder_name,
        balance=0
    ):

        self.account_number = account_number
        self.holder_name = holder_name

        self._balance = balance
        self._transactions = []

        if balance > 0:

            self._record_transaction(
                "Opening Balance",
                balance
            )

    # --------------------------------------------------------
    # TRANSACTION RECORDING
    # --------------------------------------------------------

    def _record_transaction(
        self,
        transaction_type,
        amount
    ):

        self._transactions.append({
            "type": transaction_type,
            "amount": amount,
            "balance": self._balance
        })

    # --------------------------------------------------------
    # BALANCE
    # --------------------------------------------------------

    @property
    def balance(self):

        return self._balance

    # --------------------------------------------------------
    # DEPOSIT
    # --------------------------------------------------------

    def deposit(self, amount):

        if amount <= 0:

            raise InvalidAmountError(
                "Deposit amount must be greater than zero."
            )

        self._balance += amount

        self._record_transaction(
            "Deposit",
            amount
        )

    # --------------------------------------------------------
    # WITHDRAW
    # --------------------------------------------------------

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

        self._record_transaction(
            "Withdrawal",
            amount
        )

    # --------------------------------------------------------
    # POLYMORPHIC BENEFIT
    # --------------------------------------------------------

    def calculate_benefit(self):

        return 0

    # --------------------------------------------------------
    # ACCOUNT DISPLAY
    # --------------------------------------------------------

    def show_account(self):

        print("\n" + "=" * 60)
        print("                    ACCOUNT")
        print("=" * 60)

        print(f"Bank           : {self.bank_name}")
        print(f"Account Number : {self.account_number}")
        print(f"Holder         : {self.holder_name}")
        print(f"Account Type   : {self.__class__.__name__}")
        print(f"Balance        : ₹{self._balance:.2f}")

        print("=" * 60)

    # --------------------------------------------------------
    # TRANSACTION HISTORY
    # --------------------------------------------------------

    def show_transactions(self):

        print("\n" + "=" * 75)
        print("                    TRANSACTION HISTORY")
        print("=" * 75)

        if not self._transactions:

            print("No transactions available.")

            return

        for number, transaction in enumerate(
            self._transactions,
            start=1
        ):

            print(
                f"{number:02d}. "
                f"{transaction['type']:<18}"
                f"₹{transaction['amount']:>10.2f}"
                f" | Balance: "
                f"₹{transaction['balance']:.2f}"
            )

        print("=" * 75)


class SavingsAccount(BankAccount):

    interest_rate = 4.0

    def calculate_benefit(self):

        return (
            self._balance *
            self.interest_rate /
            100
        )


class CurrentAccount(BankAccount):

    cashback_rate = 1.0

    def calculate_benefit(self):

        return (
            self._balance *
            self.cashback_rate /
            100
        )


class Bank:

    def __init__(self, name):

        self.name = name
        self.accounts = {}

    # --------------------------------------------------------
    # CREATE ACCOUNT
    # --------------------------------------------------------

    def add_account(self, account):

        if account.account_number in self.accounts:

            print(
                "❌ Account already exists."
            )

            return False

        self.accounts[
            account.account_number
        ] = account

        print(
            f"✅ Account "
            f"{account.account_number} created."
        )

        return True

    # --------------------------------------------------------
    # FIND ACCOUNT
    # --------------------------------------------------------

    def find_account(self, account_number):

        return self.accounts.get(
            account_number
        )

    # --------------------------------------------------------
    # SHOW ALL ACCOUNTS
    # --------------------------------------------------------

    def show_accounts(self):

        print("\n" + "=" * 75)
        print("                      BANK ACCOUNTS")
        print("=" * 75)

        if not self.accounts:

            print("No accounts registered.")

            return

        for account in self.accounts.values():

            print(
                f"{account.account_number:<12}"
                f"{account.holder_name:<20}"
                f"{account.__class__.__name__:<18}"
                f"₹{account.balance:>10.2f}"
            )

        print("=" * 75)


def main():

    bank = Bank(
        "Python National Bank"
    )

    # --------------------------------------------------------
    # CREATE ACCOUNTS
    # --------------------------------------------------------

    savings = SavingsAccount(
        "SAV1001",
        "Altamash",
        10000
    )

    current = CurrentAccount(
        "CUR1001",
        "Altamash",
        25000
    )

    bank.add_account(savings)
    bank.add_account(current)

    # --------------------------------------------------------
    # TRANSACTIONS
    # --------------------------------------------------------

    try:

        savings.deposit(5000)

        savings.withdraw(2500)

        current.deposit(10000)

        current.withdraw(4000)

    except (
        InvalidAmountError,
        InsufficientBalanceError
    ) as error:

        print(
            f"❌ Transaction failed: {error}"
        )

    # --------------------------------------------------------
    # ACCOUNT INFORMATION
    # --------------------------------------------------------

    savings.show_account()

    current.show_account()

    # --------------------------------------------------------
    # POLYMORPHISM
    # --------------------------------------------------------

    print("\n" + "=" * 60)
    print("                    BENEFITS")
    print("=" * 60)

    accounts = [
        savings,
        current
    ]

    for account in accounts:

        print(
            f"{account.account_number} "
            f"→ Benefit: "
            f"₹{account.calculate_benefit():.2f}"
        )

    # --------------------------------------------------------
    # TRANSACTION HISTORY
    # --------------------------------------------------------

    savings.show_transactions()

    current.show_transactions()

    # --------------------------------------------------------
    # BANK OVERVIEW
    # --------------------------------------------------------

    bank.show_accounts()


if __name__ == "__main__":
    main()