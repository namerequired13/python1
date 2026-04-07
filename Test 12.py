# Input: Ask the user for a string
text = input("Enter a string: ")

# Processing: Normalize the string (remove spaces and lowercase it)
cleaned = text.replace(" ", "").lower()

# Check if it's a palindrome
if cleaned == cleaned[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
