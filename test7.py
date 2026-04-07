#Ask the user to enter their marks for three subjects.
# Input
mark1 = float(input("Enter marks for subject 1: "))
mark2 = float(input("Enter marks for subject 2: "))
mark3 = float(input("Enter marks for subject 3: "))

# Processing
average = (mark1 + mark2 + mark3) / 3

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

# Output
print(f"Average: {average:.2f}")
print(f"Grade: {grade}")