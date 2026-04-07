#Ask the user to enter an amount in one currency(e.g., USD).
# Input
usd = float(input("Enter amount in USD: "))

# Fixed exchange rate (example: 1 USD = 0.92 EUR)
exchange_rate = 0.92

# Processing
eur = usd * exchange_rate

# Output
print("Equivalent amount in EUR:", round(eur, 2))