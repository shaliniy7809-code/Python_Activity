marks = []
valid = True

for i in range(3):
    score = int(input(f"Enter marks for subject {i + 1} (0-100): "))

    if score < 0 or score > 100:
        print("Invalid marks. Run again with marks from 0 to 100.")
        valid = False
        break

    if 30 <= score < 35:
        score = min(score + 5, 100)

    marks.append(score)

if valid and len(marks) == 3:
    total = sum(marks)
    average = total / 3

    print("\nFinal Marks:", marks)
    print("Total Marks:", total)
    print(f"Average: {average:.2f}")

    if all(score >= 35 for score in marks):
        print("Result: PASS")
    else:
        print("Result: FAIL")