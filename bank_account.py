from decimal import Decimal, ROUND_HALF_UP, InvalidOperation

class BankAccount:
    def __init__(self, account_number: int, customer_name: str, balance=0.00):
        self._account_number = account_number
        self._customer_name = customer_name
        self._balance = self._to_money(balance)
        self._status = "Active"
        self._history = []

    def _to_money(self, value):
        try:
            return Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        except (InvalidOperation, TypeError):
            return Decimal("0.00")

    def get_account_number(self):
        return self._account_number

    def get_customer_name(self):
        return self._customer_name

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        amt = self._to_money(amount)
        if amt <= 0:
            raise ValueError("Deposit must be positive.")
        self._balance += amt
        self._history.append(f"Deposited ${amt:.2f}")

    def withdraw(self, amount):
        amt = self._to_money(amount)
        if amt <= 0:
            raise ValueError("Withdrawal must be positive.")
        if amt > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amt
        self._history.append(f"Withdrew ${amt:.2f}")

    def __str__(self):
        return self.summary()

    def summary(self):
        return (
            f"Account #{self._account_number} - {self._customer_name}\n"
            f"Status: {self._status}\n"
            f"Balance: ${self._balance:.2f}\n"
        )
    
    def freeze(self):
        self._status = "Frozen"

    def unfreeze(self):
        self._status = "Active"

    def get_status(self):
        return self._status
    
    def is_overdrawn(self):
        return self._balance < Decimal("0.00")
    
    def get_history(self):
        return self._history.copy()