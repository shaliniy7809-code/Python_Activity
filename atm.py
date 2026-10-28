balance = 5000
transactions = []

n = int(input("Enter number of transactions: "))

for i in range(n):
    kind = input("Enter deposit or withdraw: ").strip().lower()
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount")
        transactions.append("Rejected: invalid amount")

    elif kind == "deposit":
        balance += amount
        transactions.append(f"Deposit: Rs. {amount:.2f}")

    elif kind == "withdraw":
        if amount <= balance and amount <= 10000:
            balance -= amount
            transactions.append(f"Withdrawal: Rs. {amount:.2f}")
        else:
            print("Withdrawal rejected")
            transactions.append("Rejected withdrawal")

    else:
        print("Invalid transaction type")
        transactions.append("Rejected: invalid type")

print("\n--- Transaction Summary ---")
for item in transactions:
    print(item)

print(f"Final Balance: Rs. {balance:.2f}")