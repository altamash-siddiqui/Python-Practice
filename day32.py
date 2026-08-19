"""
Day 32 - Python OOP
Commit 9: Factory Method with Classmethod

Concepts:
- Classes & Objects
- Encapsulation
- Inheritance
- Polymorphism
- Custom Exceptions
- Transaction History
- Class Methods
- Factory Method Pattern
"""


# ============================================================
# CUSTOM EXCEPTIONS
# ============================================================

class InsufficientBalanceError(Exception):
    """Raised when withdrawal exceeds available balance."""
    pass


class InvalidAmountError(Exception):
    """Raised when transaction amount is invalid."""
    pass


class DuplicateAccountError(Exception):
    """Raised when an account already exists."""
    pass


# ============================================================
# BASE ACCOUNT
# ============================================================

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

    # ========================================================
    # FACTORY METHOD
    # ========================================================

    @classmethod
    def create_account(
        cls,
        account_number,
        holder_name,
        initial_deposit=0
    ):
        """
        Factory method for creating an account.

        Using cls instead of the class name makes
        this method reusable by child classes.
        """

        if initial_deposit < 0:

            raise InvalidAmountError(
                "Initial deposit cannot be negative."
            )

        return cls(
            account_number,
            holder_name,
            initial_deposit
        )

    # ========================================================
    # INTERNAL TRANSACTION LOGGER
    # ========================================================

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

    # ========================================================
    # BALANCE PROPERTY
    # ========================================================

    @property
    def balance(self):

        return self._balance

    # ========================================================
    # DEPOSIT
    # ========================================================

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

    # ========================================================
    # WITHDRAW
    # ========================================================

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

    # ========================================================
    # BENEFIT
    # ========================================================

    def calculate_benefit(self):

        return 0

    # ========================================================
    # ACCOUNT DISPLAY
    # ========================================================

    def show_account(self):

        print("\n" + "=" * 60)
        print("                    ACCOUNT")
        print("=" * 60)

        print(
            f"Bank           : "
            f"{self.bank_name}"
        )

        print(
            f"Account Number : "
            f"{self.account_number}"
        )

        print(
            f"Holder         : "
            f"{self.holder_name}"
        )

        print(
            f"Account Type   : "
            f"{self.__class__.__name__}"
        )

        print(
            f"Balance        : "
            f"₹{self._balance:.2f}"
        )

        print("=" * 60)

    # ========================================================
    # TRANSACTION HISTORY
    # ========================================================

    def show_transactions(self):

        print("\n" + "=" * 75)
        print("                 TRANSACTION HISTORY")
        print("=" * 75)

        if not self._transactions:

            print(
                "No transactions available."
            )

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


# ============================================================
# SAVINGS ACCOUNT
# ============================================================

class SavingsAccount(BankAccount):

    interest_rate = 4.0

    @classmethod
    def create_account(
        cls,
        account_number,
        holder_name,
        initial_deposit=0
    ):

        if initial_deposit < 1000:

            raise InvalidAmountError(
                "Savings Account requires "
                "minimum ₹1000 initial deposit."
            )

        return cls(
            account_number,
            holder_name,
            initial_deposit
        )

    def calculate_benefit(self):

        return (
            self._balance *
            self.interest_rate /
            100
        )


# ============================================================
# CURRENT ACCOUNT
# ============================================================

class CurrentAccount(BankAccount):

    cashback_rate = 1.0

    @classmethod
    def create_account(
        cls,
        account_number,
        holder_name,
        initial_deposit=0
    ):

        if initial_deposit < 5000:

            raise InvalidAmountError(
                "Current Account requires "
                "minimum ₹5000 initial deposit."
            )

        return cls(
            account_number,
            holder_name,
            initial_deposit
        )

    def calculate_benefit(self):

        return (
            self._balance *
            self.cashback_rate /
            100
        )


# ============================================================
# BANK
# ============================================================

class Bank:

    def __init__(self, name):

        self.name = name

        self.accounts = {}

    # ========================================================
    # REGISTER ACCOUNT
    # ========================================================

    def register_account(self, account):

        if account.account_number in self.accounts:

            raise DuplicateAccountError(
                f"Account "
                f"{account.account_number} "
                f"already exists."
            )

        self.accounts[
            account.account_number
        ] = account

        print(
            f"✅ Account "
            f"{account.account_number} "
            f"registered successfully."
        )

    # ========================================================
    # FIND ACCOUNT
    # ========================================================

    def find_account(self, account_number):

        return self.accounts.get(
            account_number
        )

    # ========================================================
    # BANK OVERVIEW
    # ========================================================

    def show_accounts(self):

        print("\n" + "=" * 80)
        print("                       BANK OVERVIEW")
        print("=" * 80)

        if not self.accounts:

            print(
                "No accounts registered."
            )

            return

        print(
            f"{'Account':<15}"
            f"{'Holder':<20}"
            f"{'Type':<20}"
            f"{'Balance':>15}"
        )

        print("-" * 80)

        for account in self.accounts.values():

            print(
                f"{account.account_number:<15}"
                f"{account.holder_name:<20}"
                f"{account.__class__.__name__:<20}"
                f"₹{account.balance:>13.2f}"
            )

        print("=" * 80)


# ============================================================
# DEMO
# ============================================================

def main():

    print("\n" + "=" * 75)
    print("             PYTHON NATIONAL BANK")
    print("              OOP BANKING SYSTEM")
    print("=" * 75)

    bank = Bank(
        "Python National Bank"
    )

    # ========================================================
    # CREATE SAVINGS ACCOUNT USING FACTORY METHOD
    # ========================================================

    try:

        savings = SavingsAccount.create_account(
            account_number="SAV2001",
            holder_name="Altamash",
            initial_deposit=10000
        )

        bank.register_account(
            savings
        )

    except (
        InvalidAmountError,
        DuplicateAccountError
    ) as error:

        print(
            f"❌ Account creation failed: "
            f"{error}"
        )

    # ========================================================
    # CREATE CURRENT ACCOUNT
    # ========================================================

    try:

        current = CurrentAccount.create_account(
            account_number="CUR2001",
            holder_name="Altamash",
            initial_deposit=25000
        )

        bank.register_account(
            current
        )

    except (
        InvalidAmountError,
        DuplicateAccountError
    ) as error:

        print(
            f"❌ Account creation failed: "
            f"{error}"
        )

    # ========================================================
    # PERFORM TRANSACTIONS
    # ========================================================

    try:

        savings.deposit(5000)

        savings.withdraw(2000)

        current.deposit(10000)

        current.withdraw(5000)

    except (
        InvalidAmountError,
        InsufficientBalanceError
    ) as error:

        print(
            f"❌ Transaction failed: "
            f"{error}"
        )

    # ========================================================
    # DISPLAY ACCOUNTS
    # ========================================================

    savings.show_account()

    current.show_account()

    # ========================================================
    # POLYMORPHIC BENEFITS
    # ========================================================

    print("\n" + "=" * 60)
    print("                  ACCOUNT BENEFITS")
    print("=" * 60)

    for account in bank.accounts.values():

        benefit = (
            account.calculate_benefit()
        )

        print(
            f"{account.account_number} "
            f"→ ₹{benefit:.2f}"
        )

    # ========================================================
    # TRANSACTION HISTORY
    # ========================================================

    savings.show_transactions()

    current.show_transactions()

    # ========================================================
    # BANK OVERVIEW
    # ========================================================

    bank.show_accounts()

    print("\n" + "=" * 75)
    print("                  SYSTEM COMPLETE")
    print("=" * 75)


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":

    main()