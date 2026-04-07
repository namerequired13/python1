#Prompt the user to enter the principal amount, interest rate (in percentage), and the time period (in years)
# Input
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate (in %): "))
time = float(input("Enter the time period (in years): "))

# Processing
simple_interest = (principal * rate * time) / 100

# Output
print("The Simple Interest is:", simple_interest)