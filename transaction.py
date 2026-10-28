ids = []
amounts = []

for i in range(5):
    tid = input("Enter transaction ID: ").strip()
    amount = float(input("Enter transaction amount: "))

    ids.append(tid)
    amounts.append(amount)

print("\n--- Transaction Audit ---")
found = False

for i in range(len(ids)):
    if ids.count(ids[i]) > 1 and ids[i] not in ids[:i]:
        print("Duplicate transaction ID:", ids[i])
        found = True

    if amounts[i] > 10000:
        print("Large transaction:", ids[i],
              "Amount:", amounts[i])
        found = True

if not found:
    print("No suspicious transactions found")