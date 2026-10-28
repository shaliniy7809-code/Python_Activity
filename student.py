subjects = ["Python", "Maths", "English"]
previous = []
latest = []

for subject in subjects:
    score = int(input(f"Previous marks in {subject} (0-100): "))
    previous.append(score)

for subject in subjects:
    score = int(input(f"Latest marks in {subject} (0-100): "))
    latest.append(score)

print("\n--- Performance Report ---")

for i, subject in enumerate(subjects):
    change = latest[i] - previous[i]
    print(f"{subject} change: {change}")

    if latest[i] < 40:
        print("Weak subject:", subject)
    elif change > 0:
        print("Performance improved")
    elif change < 0:
        print("Performance declined")
    else:
        print("No change")

average = sum(latest) / len(latest)
print(f"Latest Average: {average:.2f}")

if average >= 75:
    print("Classification: Excellent")
elif average >= 50:
    print("Classification: Good")
else:
    print("Classification: Needs Improvement")