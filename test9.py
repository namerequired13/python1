# Input: Ask the user to enter their age
age = int(input("Enter your age: "))

# Processing: Determine the age category
if age < 18:
    category = "Minor"
elif 18 <= age <= 65:
    category = "Adult"
else:
    category = "Senior citizen"

# Output: Display the category
print("You are classified as:", category)
