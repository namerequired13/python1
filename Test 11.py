# Input: Ask the user for the number of rows
rows = int(input("Enter the number of rows: "))

# Processing & Output: Print the right triangle pattern
for i in range(1, rows + 1):
    print("*" * i)
