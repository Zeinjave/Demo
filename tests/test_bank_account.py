# tests/test_bank_account.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from bank_account import BankAccount

def test_account():
    acct = BankAccount(987654, "John Smith", 200.00)
    acct.deposit(100.00)
    acct.withdraw(50.00)
    assert acct.get_balance() == 250.00

if __name__ == "__main__":
    test_account()
    print("✅ BankAccount test passed.")
