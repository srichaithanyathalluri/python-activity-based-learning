
# Multi-Currency Travel Budget Analysis

budget = float(input("Enter your total budget in INR: "))

# Exchange rates: 1 unit of foreign currency in INR
rates = {
    "USD": 85.0,
    "EUR": 92.0,
    "GBP": 110.0,
    "INR": 1.0
}

expenses = {}

n = int(input("Enter number of expense categories: "))

for i in range(n):
    print("\nExpense category", i + 1)

    category = input("Enter category (Hotel/Food/Travel/Shopping): ")
    amount = float(input("Enter expense amount: "))
    currency = input("Enter currency (USD/EUR/GBP/INR): ").upper()

    if currency not in rates:
        print("Unsupported currency! Expense skipped.")
        continue

    fee_percent = float(input("Enter conversion fee percentage: "))

    # Convert expense into INR
    converted_amount = amount * rates[currency]

    # Add conversion fee for foreign currencies
    if currency != "INR":
        fee = converted_amount * fee_percent / 100
    else:
        fee = 0

    total = converted_amount + fee

    expenses[category] = expenses.get(category, 0) + total

    print("Converted amount: Rs.", round(converted_amount, 2))
    print("Conversion fee: Rs.", round(fee, 2))
    print("Total expense: Rs.", round(total, 2))

# Calculate total spending
total_spending = sum(expenses.values())

print("\n----- TRAVEL BUDGET SUMMARY -----")

for category, amount in expenses.items():
    print(category, ": Rs.", round(amount, 2))

print("Total spending: Rs.", round(total_spending, 2))
print("Budget: Rs.", round(budget, 2))

if total_spending > budget:
    print("Budget exceeded by Rs.", round(total_spending - budget, 2))
else:
    print("Remaining budget: Rs.", round(budget - total_spending, 2))

# Find largest expense category
if expenses:
    largest = max(expenses, key=expenses.get)
    print("Largest expense category:", largest)
    print("Amount: Rs.", round(expenses[largest], 2))
else:
    print("No valid expenses entered.")
