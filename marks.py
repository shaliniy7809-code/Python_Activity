students = ["Asha", "Balu", "Charan"]
subjects = ["Python", "Maths", "English"]

marks = [
    [80, 75, 90],
    [60, 55, 65],
    [35, 45, 50]
]

print("--- Student Marks Matrix ---")

for i, student in enumerate(students):
    total = sum(marks[i])
    average = total / len(subjects)
    print(f"{student}: marks={marks[i]}, total={total}, average={average:.2f}")

print("\n--- Subject Averages ---")

for j, subject in enumerate(subjects):
    subject_total = sum(row[j] for row in marks)
    print(f"{subject}: {subject_total / len(students):.2f}")

top_index = max(range(len(students)), key=lambda i: sum(marks[i]))
print("\nTop Performer:", students[top_index])