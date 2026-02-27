# Input section
name = input("Enter student name: ")
mark1 = float(input("Enter marks for subject 1: "))
mark2 = float(input("Enter marks for subject 2: "))
mark3 = float(input("Enter marks for subject 3: "))

# Calculation section
total = mark1 + mark2 + mark3
percentage = (total / 300) * 100

# Grade Logic
if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
elif percentage < 40:
    grade = "F"

# Output section
print(f"\n--- Student Report ---")
print(f"Name: {name}")
print(f"Total Marks: {total}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
