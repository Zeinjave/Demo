import csv
from safe_decimal import summarize_transactions

def load_transactions_from_csv(filepath="data/test_transactions.csv"):
    transactions = []
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            transactions.append(row.get("amount"))  # could be string, number, or invalid
    return transactions

def main():
    tx_list = load_transactions_from_csv("data/test_transactions.csv")
    result = summarize_transactions(tx_list)

    print("Transaction Summary:")
    for key, value in result.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()