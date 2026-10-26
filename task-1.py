
# Progressive Electricity Billing

def calculate_bill(units):
    # Electricity charges based on consumption slabs
    if units <= 100:
        energy_charge = units * 1.50
    elif units <= 200:
        energy_charge = (100 * 1.50) + (units - 100) * 2.50
    elif units <= 300:
        energy_charge = (100 * 1.50) + (100 * 2.50) + (units - 200) * 4.00
    else:
        energy_charge = (100 * 1.50) + (100 * 2.50) + (100 * 4.00) + (units - 300) * 6.00

    fixed_charge = 50
    surcharge = energy_charge * 0.05
    subtotal = energy_charge + fixed_charge + surcharge

    # Apply 5% rebate if usage is at most 100 units
    rebate = subtotal * 0.05 if units <= 100 else 0

    total_bill = subtotal - rebate
    return round(total_bill, 2)


# Bills for three months
months = ["Month 1", "Month 2", "Month 3"]
bills = []

for month in months:
    units = int(input(f"Enter units for {month}: "))
    bill = calculate_bill(units)
    bills.append(bill)
    print(f"{month} Bill: Rs. {bill:.2f}")

# Compare bills and identify unusual increases
print("\nMonthly Bill Comparison:")

for i in range(1, len(bills)):
    increase = bills[i] - bills[i - 1]

    if bills[i - 1] > 0:
        percentage = (increase / bills[i - 1]) * 100
    else:
        percentage = 0

    print(f"{months[i - 1]} to {months[i]}: "
          f"Rs. {increase:.2f} change")

    if percentage > 30:
        print("Warning: Unusual increase in electricity bill!")
