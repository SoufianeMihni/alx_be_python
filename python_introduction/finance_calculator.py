# Prompt user for monthly income
monthly_income = float(input("Enter your monthly income: "))

# Prompt user for total monthly expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project annual savings with interest
annual_savings = monthly_savings * 12
projected_annual_savings = annual_savings + (annual_savings * 0.05)

# Display results
print(f"Your monthly savings are: {monthly_savings:.2f}")
print(f"Your projected annual savings after interest are: {projected_annual_savings:.2f}")
