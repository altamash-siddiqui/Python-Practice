"""
Day 33 - Transaction Filter Utility

Provides filtering utilities for bank
transaction history.
"""


def filter_transactions(
    account,
    transaction_type=None,
    minimum_amount=None
):
    """Filter account transactions."""

    transactions = account._transactions

    if transaction_type is not None:
        transactions = [
            transaction
            for transaction in transactions
            if transaction["type"].lower()
            == transaction_type.lower()
        ]

    if minimum_amount is not None:
        transactions = [
            transaction
            for transaction in transactions
            if transaction["amount"] >= minimum_amount
        ]

    return transactions


def display_transactions(transactions):
    """Display filtered transactions."""

    if not transactions:
        print("No matching transactions found.")
        return

    print("\n" + "=" * 60)
    print("             FILTERED TRANSACTIONS")
    print("=" * 60)

    for number, transaction in enumerate(
        transactions,
        start=1
    ):
        print(
            f"{number}. "
            f"{transaction['type']} | "
            f"₹{transaction['amount']:.2f} | "
            f"Balance: ₹{transaction['balance']:.2f}"
        )

    print("=" * 60)


if __name__ == "__main__":

    from day32 import SavingsAccount

    account = SavingsAccount.create_account(
        "SAV3306",
        "Altamash",
        10000
    )

    account.deposit(3000)
    account.deposit(5000)
    account.withdraw(2000)

    print("\nDeposit Transactions:")

    deposits = filter_transactions(
        account,
        transaction_type="Deposit"
    )

    display_transactions(deposits)

    print("\nTransactions Above ₹2500:")

    large_transactions = filter_transactions(
        account,
        minimum_amount=2500
    )

    display_transactions(large_transactions)