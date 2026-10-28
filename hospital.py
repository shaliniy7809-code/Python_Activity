name = input("Enter patient name: ")
consultation = float(input("Enter consultation charge: "))
diagnostic = float(input("Enter diagnostic charge: "))
treatment = float(input("Enter treatment charge: "))

total = consultation + diagnostic + treatment
concession = total * 0.10 if total >= 5000 else 0
final_bill = total - concession

print("\n--- Hospital Bill ---")
print("Patient Name:", name)
print(f"Total Bill: Rs. {total:.2f}")
print(f"Concession: Rs. {concession:.2f}")
print(f"Final Bill: Rs. {final_bill:.2f}")
print("Classification:", "High Bill" if final_bill >= 4000 else "Normal Bill")