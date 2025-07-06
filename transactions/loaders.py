import csv
import json

def load_transactions_from_csv(filepath="data/test_transactions.csv"):
    transactions = []
    skipped_rows = []

    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for i, row in enumerate(reader, start=1):
            amount = row.get("amount")
            if amount is None:
                skipped_rows.append((i, amount))
                continue
            try:
                transactions.append(float(amount))
            except (ValueError, TypeError):
                skipped_rows.append((i, amount))

    if skipped_rows:
        print(f"\n⚠️ Skipped {len(skipped_rows)} rows due to invalid values:")
        for row_num, bad_value in skipped_rows:
            print(f"  - Row {row_num}: invalid amount '{bad_value}'")
    
    return transactions

def load_transactions_from_json(filepath="data/test_transactions.json"):
    transactions = []
    skipped_items = []

    with open(filepath) as jsonfile:
        try:
            data = json.load(jsonfile)
        except json.JSONDecodeError as e:
            print(f"❌ Failed to parse JSON: {e}")
            return []

        for i, entry in enumerate(data, start=1):
            amount = entry.get("amount")
            if amount is None:
                skipped_items.append((i, amount))
                continue
            try:
                transactions.append(float(amount))
            except (ValueError, TypeError):
                skipped_items.append((i, amount))

    if skipped_items:
        print(f"\n⚠️ Skipped {len(skipped_items)} entries in JSON:")
        for i, bad in skipped_items:
            print(f"  - Entry {i}: invalid amount '{bad}'")

    return transactions