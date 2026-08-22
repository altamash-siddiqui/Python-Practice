"""
Day 33 - Banking System Input Validation

Provides reusable validation helpers for
account numbers, holder names and transaction amounts.
"""


def validate_account_number(account_number):
    """Validate a bank account number."""

    if not isinstance(account_number, str):
        return False

    account_number = account_number.strip()

    return (
        len(account_number) >= 4
        and account_number.replace("-", "").isalnum()
    )


def validate_holder_name(holder_name):
    """Validate account holder name."""

    if not isinstance(holder_name, str):
        return False

    holder_name = holder_name.strip()

    return (
        len(holder_name) >= 2
        and all(
            character.isalpha() or character.isspace()
            for character in holder_name
        )
    )


def validate_amount(amount):
    """Validate positive transaction amount."""

    return isinstance(amount, (int, float)) and amount > 0


if __name__ == "__main__":

    print("Account:", validate_account_number("SAV3301"))
    print("Holder:", validate_holder_name("Altamash Siddiqui"))
    print("Amount:", validate_amount(5000))