password = input("Enter a sample password: ")
issues = []

if len(password) < 8:
    issues.append("Minimum 8 characters required")

if not any(ch.islower() for ch in password):
    issues.append("Add a lowercase letter")

if not any(ch.isupper() for ch in password):
    issues.append("Add an uppercase letter")

if not any(ch.isdigit() for ch in password):
    issues.append("Add a number")

if not any(ch in "@#$!" for ch in password):
    issues.append("Add a special character (@, #, $, !)")

if "password" in password.lower():
    issues.append("Do not use the word 'password'")

print("\n--- Password Validation ---")

if issues:
    print("Password is NOT valid")
    for issue in issues:
        print("-", issue)
else:
    print("Password meets all sample rules")