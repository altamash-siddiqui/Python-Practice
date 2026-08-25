"""
Day 34 - Bank Analytics & Reporting

Builds analytical reports on top of the
Day 32 OOP banking system.
"""

from day32 import (
    Bank,
    SavingsAccount,
    CurrentAccount,
)


class BankAnalytics:

    def __init__(self, bank):
        self.bank = bank

    def account_count(self):
        """Return total number of accounts."""
        return len(self.bank.accounts)

    def total_balance(self):
        """Return combined balance of all accounts."""

        return sum(
            account.balance
            for account in self.bank.accounts.values()
        )
        
    def average_balance(self):
        """Return average account balance."""

        count = self.account_count()

        if count == 0:
            return 0

        return self.total_balance() / count
    
    def transaction_count(self):
        """Return total number of recorded transactions."""

        return sum(
            len(account._transactions)
            for account in self.bank.accounts.values()
        )
        
    def account_type_summary(self):
        """Return account counts grouped by type."""

        summary = {}

        for account in self.bank.accounts.values():

            account_type = account.__class__.__name__

            summary[account_type] = (
                summary.get(account_type, 0) + 1
            )

        return summary
    
    def highest_balance_account(self):
        """Return account with the highest balance."""

        accounts = list(
            self.bank.accounts.values()
        )

        if not accounts:
            return None

        return max(
            accounts,
            key=lambda account: account.balance
        )


if __name__ == "__main__":

    bank = Bank("Python National Bank")

    savings = SavingsAccount.create_account(
        "SAV3401",
        "Altamash",
        10000
    )

    current = CurrentAccount.create_account(
        "CUR3401",
        "Rahul",
        15000
    )

    bank.register_account(savings)
    bank.register_account(current)
    
    savings.deposit(2000)
    savings.withdraw(1000)

    current.deposit(5000)

    analytics = BankAnalytics(bank)

    print(
        f"Total Accounts: "
        f"{analytics.account_count()}"
    )

    print(
        f"Total Balance: "
        f"₹{analytics.total_balance():.2f}"
    )
    
    print(
        f"Average Balance: "
        f"₹{analytics.average_balance():.2f}"
    )
    
    print(
        f"Total Transactions: "
        f"{analytics.transaction_count()}"
    )
    
    print("\nAccount Type Summary:")

    for account_type, count in (
        analytics.account_type_summary().items()
    ):
        print(
            f"{account_type}: {count}"
        )
        
        highest = analytics.highest_balance_account()

    if highest:

        print("\nHighest Balance Account:")

        print(
            f"Account: {highest.account_number}"
        )

        print(
            f"Holder: {highest.holder_name}"
        )

        print(
            f"Balance: ₹{highest.balance:.2f}"
        )