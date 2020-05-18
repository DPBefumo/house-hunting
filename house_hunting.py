# Please make your program print results in the format shown in the test cases below.

# Hints
# To help you get started, here is a rough outline of the stages you should probably follow in writing your code:

# - Retrieve user input. Look at `input()` if you need help with getting user input. For this problem set, you can assume that users will enter valid input (e.g. they won’t enter a string when you expect a number.)
# - Initialize some state variables. You should decide what information you need. Be careful about values that represent annual amounts and those that represent monthly amounts.
# - Try different inputs and see how long it takes to save for a down payment.

# 1
total_cost = input("Total cost of your home:")
print("Total cost of your dream is: ", total_cost)

# 2
portion_down_payment = float(total_cost)*.25
print("Your down payment will need to be: ", portion_down_payment)

# 3
current_savings = input("Current savings in the bank:")
print("Your savings for your house is: ", current_savings)

# 4
r = 0.04
increase_monthly_savings = int(current_savings)*r/12
print("You will increase your savings monthly by: ", increase_monthly_savings)

# 5. Call your annual salary `annual_salary​`.
annual_salary = input("Current annual salary:")
print("Your annual salary is: ", annual_salary)


# 6. Assume you are going to dedicate a certain amount of your salary each month to saving for the down payment. `Call that portion_saved`​. This variable should be in decimal form (i.e. 0.1 for 10%).


# 7. At the end of each month, your savings will be increased by the return on your investment, plus a percentage of your monthly salary ​(annual salary / 12).


# Write a program to calculate how many months it will take you to save up enough money for a down payment.
    # Your program should ask the user to enter the following variables:
    # 1. The starting annual salary (`annual_salary`)
    # 2. The portion of salary to be saved (`portion_saved`)
    # 3. The cost of your dream home (`total_cost`)

# while current_savings < portion_down_payment: