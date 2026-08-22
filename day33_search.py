"""
Day 33 - Account Search Utility

Provides search functionality for the
Bank class.
"""


def search_accounts(bank, keyword):
    """Search accounts by number or holder name."""

    keyword = str(keyword).strip().lower()

    results = []

    for account in bank.accounts.values():

        account_number = (
            str(account.account_number).lower()
        )

        holder_name = (
            str(account.holder_name).lower()
        )

        if (
            keyword in account_number
            or keyword in holder_name
        ):

            results.append(account)

    return results


def display_search_results(accounts):
    """Display matching accounts."""

    if not accounts:

        print("No matching accounts found.")

        return

    print("\n" + "=" * 65)
    print("                  SEARCH RESULTS")
    print("=" * 65)

    for account in accounts:

        print(
            f"Account : {account.account_number}"
        )

        print(
            f"Holder  : {account.holder_name}"
        )

        print(
            f"Type    : {account.__class__.__name__}"
        )

        print(
            f"Balance : ₹{account.balance:.2f}"
        )

        print("-" * 65)


if __name__ == "__main__":

    from day32 import (
        Bank,
        SavingsAccount,
        CurrentAccount
    )

    bank = Bank("Python National Bank")

    bank.register_account(
        SavingsAccount.create_account(
            "SAV3304",
            "Altamash",
            10000
        )
    )

    bank.register_account(
        CurrentAccount.create_account(
            "CUR3304",
            "Rahul",
            5000
        )
    )

    matches = search_accounts(
        bank,
        "Altamash"
    )

    display_search_results(matches)
