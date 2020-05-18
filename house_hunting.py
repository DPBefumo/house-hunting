# Please make your program print results in the format shown in the test cases below.

# Hints
# To help you get started, here is a rough outline of the stages you should probably follow in writing your code:

# - Retrieve user input. Look at `input()` if you need help with getting user input. For this problem set, you can assume that users will enter valid input (e.g. they won’t enter a string when you expect a number.)
# - Initialize some state variables. You should decide what information you need. Be careful about values that represent annual amounts and those that represent monthly amounts.
# - Try different inputs and see how long it takes to save for a down payment.

annual_salary = float(input("Current annual salary:"))
print("Your annual salary is: ", annual_salary)

percentage_saved = float(input("How much do you want to save out of your salary?"))
print("You are going to save ", percentage_saved, "of your salary" )

salary_saved = annual_salary * percentage_saved / 12
print("Amount saved each month from salary: ", salary_saved)

current_savings = float(input("Current savings in the bank:"))
print("Your savings for your house is: ", current_savings)

r = 0.04
return_on_investment = current_savings*r/12
print("You will increase your savings monthly by: ", return_on_investment)

increase_monthly_savings = salary_saved+return_on_investment
print("Each month you are saving: ", increase_monthly_savings)

total_cost = float(input("Total cost of your home:"))
print("Total cost of your dream is: ", total_cost)

portion_down_payment = total_cost*.25
print("Your down payment will need to be: ", portion_down_payment)

# Write a program to calculate how many months it will take you to save up enough money for a down payment.
    # Your program should ask the user to enter the following variables:
    # 1. The starting annual salary (`annual_salary`)
    # 2. The portion of salary to be saved (`portion_saved`)
    # 3. The cost of your dream home (`total_cost`)

# while current_savings < portion_down_payment: