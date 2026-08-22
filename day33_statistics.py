"""
Day 33 - Transaction Statistics

Provides basic transaction analytics
for bank accounts.
"""


def transaction_statistics(account):
    """Calculate transaction statistics."""

    deposits = [
        transaction
        for transaction in account._transactions
        if transaction["type"] in (
            "Deposit",
            "Opening Balance"
        )
    ]

    withdrawals = [
        transaction
        for transaction in account._transactions
        if transaction["type"] == "Withdrawal"
    ]

    total_deposits = sum(
        transaction["amount"]
        for transaction in deposits
    )

    total_withdrawals = sum(
        transaction["amount"]
        for transaction in withdrawals
    )

    return {
        "transaction_count": len(account._transactions),
        "deposit_count": len(deposits),
        "withdrawal_count": len(withdrawals),
        "total_deposits": total_deposits,
        "total_withdrawals": total_withdrawals,
        "current_balance": account.balance,
    }


def show_statistics(account):
    """Display account transaction statistics."""

    statistics = transaction_statistics(account)

    print("\n" + "=" * 55)
    print("             TRANSACTION STATISTICS")
    print("=" * 55)

    print(
        f"Total Transactions : "
        f"{statistics['transaction_count']}"
    )

    print(
        f"Deposits           : "
        f"{statistics['deposit_count']}"
    )

    print(
        f"Withdrawals        : "
        f"{statistics['withdrawal_count']}"
    )

    print(
        f"Total Deposits     : "
        f"₹{statistics['total_deposits']:.2f}"
    )

    print(
        f"Total Withdrawals  : "
        f"₹{statistics['total_withdrawals']:.2f}"
    )

    print(
        f"Current Balance    : "
        f"₹{statistics['current_balance']:.2f}"
    )

    print("=" * 55)


if __name__ == "__main__":

    from day32 import SavingsAccount

    account = SavingsAccount.create_account(
        "SAV3302",
        "Altamash",
        10000
    )

    account.deposit(3000)
    account.withdraw(1500)

    show_statistics(account)