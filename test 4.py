#Prompt the user to enter a time duration in hours.
# Input
hours = float(input("Enter time in hours: "))

# Processing
minutes = hours * 60
seconds = hours * 3600

# Output
print("Time in minutes:", minutes)
print("Time in seconds:", seconds)