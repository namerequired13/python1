# Input: Ask the user for a positive integer
num = int(input("Enter a positive integer: "))

# Make sure the number is positive
if num <= 0:
    print("Please enter a number greater than 0.")
else:
    print("Collatz sequence:")
    print(num)

    # Processing: Generate the Collatz sequence
    while num != 1:
        if num % 2 == 0:
            num = num // 2        # Even rule
        else:
            num = 3 * num + 1     # Odd rule

        print(num)  # Output each step

