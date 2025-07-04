#import
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

#ToMoney Function
def to_money(value) -> Decimal:
    return Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

#AddMoney function
def add_money(a, b) -> Decimal:
    return to_money(to_money(a) + to_money(b))

#SubtractMoney function
def subtract_money(a, b) -> Decimal:
    return to_money(to_money(a) - to_money(b))

#Summarize transactions function
def summarize_transactions(transactions: list) -> dict:
    balance = Decimal("0.00")
    total_deposits = Decimal("0.00")
    total_withdrawals = Decimal("0.00")
    skipped = []

    for tx in transactions:
        try:
            amount = to_money(tx)
            balance += amount
            if amount > 0:
                total_deposits += amount
            elif amount < 0:
                total_withdrawals += abs(amount)
        except (InvalidOperation, ValueError, TypeError):
            skipped.append(tx)

    return {
        "final_balance": balance,
        "total_deposits": total_deposits,
        "total_withdrawals": total_withdrawals,
        "skipped_inputs": skipped,
    }