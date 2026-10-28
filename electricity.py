# Electricity Bill Calculator

name = input("Enter consumer name: ")
units = float(input("Enter electricity units consumed: "))

if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = (100 * 2) + (units - 100) * 3
else:
    bill = (100 * 2) + (100 * 3) + (units - 200) * 5

if bill > 1000:
    surcharge = bill * 0.05
else:
    surcharge = 0

total_bill = bill + surcharge

print("\n--- ELECTRICITY BILL ---")
print("Consumer Name:", name)
print("Units Consumed:", units)
print("Electricity Charge: Rs.", bill)
print("Surcharge: Rs.", surcharge)
print("Total Bill: Rs.", total_bill)
