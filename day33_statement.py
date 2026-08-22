"""
Day 33 - Account Statement Generator

Generates a readable statement from
an existing BankAccount object.
"""


def generate_statement(account):
    """Generate a formatted account statement."""

    lines = []

    lines.append("=" * 65)
    lines.append("                 ACCOUNT STATEMENT")
    lines.append("=" * 65)

    lines.append(
        f"Bank           : {account.bank_name}"
    )

    lines.append(
        f"Account Number : {account.account_number}"
    )

    lines.append(
        f"Holder         : {account.holder_name}"
    )

    lines.append(
        f"Account Type   : {account.__class__.__name__}"
    )

    lines.append("-" * 65)

    lines.append(
        f"{'No.':<6}"
        f"{'Transaction':<20}"
        f"{'Amount':>12}"
        f"{'Balance':>15}"
    )

    lines.append("-" * 65)

    for number, transaction in enumerate(
        account._transactions,
        start=1
    ):

        lines.append(
            f"{number:<6}"
            f"{transaction['type']:<20}"
            f"₹{transaction['amount']:>10.2f}"
            f"₹{transaction['balance']:>13.2f}"
        )

    lines.append("-" * 65)

    lines.append(
        f"Current Balance : ₹{account.balance:.2f}"
    )

    lines.append("=" * 65)

    return "\n".join(lines)


if __name__ == "__main__":

    from day32 import SavingsAccount

    account = SavingsAccount.create_account(
        "SAV3301",
        "Altamash",
        10000
    )

    account.deposit(2500)
    account.withdraw(1000)

    print(generate_statement(account))