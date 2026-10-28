total = 0

for i in range(3):
    print("\nProduct", i + 1)
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    amount = price * quantity
    total += amount
    print(f"{name} amount: Rs. {amount:.2f}")

discount = total * 0.10 if total >= 2000 else 0
final = total - discount

print("\n--- Retail Bill ---")
print(f"Total: Rs. {total:.2f}")
print(f"Discount: Rs. {discount:.2f}")
print(f"Final Amount: Rs. {final:.2f}")