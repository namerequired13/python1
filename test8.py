# Ask the user to enter a single character
char = input("Enter a single character: ").lower()

# Check if it's a vowel or consonant
if char in ['a', 'e', 'i', 'o', 'u']:
    print("The character is a vowel.")
else:
    print("The character is a consonant.")