# Problem 1 - Quantity Pricing

quantity = int(input("Enter quantity: "))

if quantity >= 1000:
    unit_price = 3.00
else:
    unit_price = 5.00

extended_price = quantity * unit_price
tax = extended_price * 0.07
total = extended_price + tax

print()
print(f"{'Quantity':<15}{'Unit Price':>12}{'Extended Price':>17}{'Tax':>12}{'Total':>12}")
print(f"{quantity:<15}{unit_price:>12.2f}{extended_price:>17.2f}{tax:>12.2f}{total:>12.2f}")