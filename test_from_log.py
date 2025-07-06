from transactions import load_transactions_from_csv, load_transactions_from_json
from safe_decimal import summarize_transactions

def main():
    print("Choose input file type:")
    print("1. CSV")
    print("2. JSON")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        tx_list = load_transactions_from_csv()
    elif choice == "2":
        tx_list = load_transactions_from_json()
    else:
        print("❌ Invalid choice.")
        return

    result = summarize_transactions(tx_list)
    print("\nTransaction Summary:")
    for key, value in result.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
