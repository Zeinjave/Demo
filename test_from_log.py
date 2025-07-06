from transactions import load_transactions_from_csv, load_transactions_from_json
from safe_decimal import summarize_transactions

def main():
    tx_list = load_transactions_from_csv("data/test_transactions.csv")
    result = summarize_transactions(tx_list)

    print("Transaction Summary:")
    for key, value in result.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
