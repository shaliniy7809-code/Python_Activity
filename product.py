products = [
    ("P101", 250.0, 10),
    ("P102", 120.0, 3),
    ("P103", 500.0, 0),
    ("P104", -50.0, 5)
]

print("--- Product Catalogue Audit ---")

for product in products:
    product_id, price, quantity = product

    if price < 0 or quantity < 0:
        print(product_id, "Invalid product record")
        continue

    value = price * quantity
    print(f"{product_id}: price=Rs. {price:.2f}, stock={quantity}, inventory value=Rs. {value:.2f}")

    if quantity < 5:
        print("  Replenishment required")

print("\nAudit completed.")