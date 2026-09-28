''' This program focuses on calculating the fixed-income total investment revenue. '''

# Constant Values
COMPOUND_PERIOD = 12    # 12 is used as the compound period since revenue will be calculated monthly.

# Input monthly investment value that is positive
while (monthly_investment := float(input("Enter monthly investment amount: "))) < 0:
    print("Invalid: Monthly investment amount must be a positive number.")

# Input yearly interest value that is positive
while (yearly_interest_rate := float(input("Enter yearly interest rate: "))) < 0:
    print("Invalid: Yearly interest rate value must be a positive number.")

# Input investment years value that is positive
while (investment_years := int(input("How many years to invest?: "))) < 0:
    print("Invalid: Investment years value must be a positive number.")

# Total investment revenue that will start off with assigned value of 0
total_investment_revenue = 0

for month in range(investment_years * COMPOUND_PERIOD):
    # Calculating the compound investment
    compound_investment_calcuation = (1 + ((yearly_interest_rate / 100) / COMPOUND_PERIOD))

    # Add the monthly investment each time to the total investment revenue before multiplying by the compound interest 
    total_investment_revenue = (total_investment_revenue + monthly_investment) * (compound_investment_calcuation)

    # Print current month with the current total investment value
    print(f"Month {month + 1} revenue: {total_investment_revenue}")

# Print the total investment revenue after the number of years alongside the yearly rate.
print(f"After {investment_years} years, you will receive a total investment revenue of ${total_investment_revenue:,.2f} at a yearly rate of {yearly_interest_rate}")