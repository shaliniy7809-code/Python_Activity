name = input("Enter employee name: ")
basic = float(input("Enter basic salary: "))
hours = int(input("Enter overtime hours: "))

allowance = basic * 0.20
overtime = hours * 200
gross = basic + allowance + overtime
deduction = gross * 0.10
net = gross - deduction

print("\n--- Salary Statement ---")
print("Employee:", name)
print(f"Basic Salary: Rs. {basic:.2f}")
print(f"Allowance: Rs. {allowance:.2f}")
print(f"Overtime Pay: Rs. {overtime:.2f}")
print(f"Gross Salary: Rs. {gross:.2f}")
print(f"Deduction: Rs. {deduction:.2f}")
print(f"Net Salary: Rs. {net:.2f}")