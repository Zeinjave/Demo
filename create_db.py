import sqlite3

#connect to SQLite
conn = sqlite3.connect("banking.db")
cursor = conn.cursor()

#CustomerAccounts Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS CustomerAccounts (
    CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
    AccountNumber NUMBER UNIQUE,
    CustomerName TEXT NOT NULL,
    CustomerPhone TEXT,
    CustomerEmail TEXT,
    CustomerAddress TEXT,
    DateOpened DATE DEFAULT CURRENT_DATE,
    AccountType TEXT DEFAULT 'Checking',
    AccountBalance REAL DEFAULT 0.00,
    AccountStatus TEXT DEFAULT 'Active'
)
""")

#Generate next available account number
def get_next_acct_number(cursor):
    cursor.execute("SELECT MAX(AccountNumber) FROM CustomerAccounts")
    result = cursor.fetchone()[0]
    return (result or 10000001) + 1 #start from 10000001

#Insert customer with generated account number
def insert_customer(name, phone=None, email=None, address=None, balance='0.00', account_type='Checking'):
    account_number = get_next_acct_number(cursor)
    cursor.execute("""
        INSERT INTO CustomerAccounts (
            AccountNumber, CustomerName, CustomerPhone, CustomerEmail, CustomerAddress, AccountType, AccountBalance
        ) Values (?, ?, ?, ?, ?, ?, ?)
    """, (account_number, name, phone, email, address, account_type, balance))
    print(f"Inserted {name} with Account Number {account_number}")

#Sample Data
insert_customer("Alice Wonderland", "903-280-1234", "alicewonder@example.com", "123 Main St", 1000.00)
insert_customer("Alice Wonderland", "903-280-1234", "alicewonder@example.com", "123 Main St", 1000.00, "Savings")
insert_customer("Cheshire Cat", "903-691-1234", "catsrule9000@example.com", "404 Lost Ave")
insert_customer("Tweedle Dee", "123-456-7890")
insert_customer("Tweedle Dum", "123-456-7890", "alicewonder@example.com", "404 Lost Ave", 500.00)

#save and close
conn.commit()
conn.close()

print("Database created and sample customers inserted.")