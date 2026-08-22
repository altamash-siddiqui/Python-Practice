"""
Day 33 - Test Suite

Tests Day 33 banking utilities.
"""

import os
import unittest

from day32 import SavingsAccount, Bank

from day33_validator import (
    validate_account_number,
    validate_holder_name,
    validate_amount,
)

from day33_statistics import (
    transaction_statistics,
)

from day33_search import (
    search_accounts,
)


class TestDay33(unittest.TestCase):

    def setUp(self):

        self.account = SavingsAccount.create_account(
            "SAV3305",
            "Altamash",
            10000
        )

        self.account.deposit(3000)
        self.account.withdraw(1000)

    def test_account_validation(self):

        self.assertTrue(
            validate_account_number("SAV3305")
        )

        self.assertTrue(
            validate_holder_name("Altamash Siddiqui")
        )

        self.assertTrue(
            validate_amount(500)
        )

    def test_invalid_account_number(self):

        self.assertFalse(
            validate_account_number("12")
        )

    def test_transaction_statistics(self):

        statistics = transaction_statistics(
            self.account
        )

        self.assertEqual(
            statistics["transaction_count"],
            3
        )

        self.assertEqual(
            statistics["total_deposits"],
            13000
        )

        self.assertEqual(
            statistics["total_withdrawals"],
            1000
        )

        self.assertEqual(
            statistics["current_balance"],
            12000
        )

    def test_account_search(self):

        bank = Bank(
            "Python National Bank"
        )

        bank.register_account(
            self.account
        )

        results = search_accounts(
            bank,
            "Altamash"
        )

        self.assertEqual(
            len(results),
            1
        )

        self.assertEqual(
            results[0].account_number,
            "SAV3305"
        )


if __name__ == "__main__":

    unittest.main()