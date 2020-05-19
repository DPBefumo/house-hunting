annual_salary = float(input("Current annual salary:"))
percentage_saved = float(input("How much do you want to save out of your salary?"))
current_savings = float(input("Current savings in the bank:"))
total_cost = float(input("Total cost of your home:"))
r = 0.04/12

salary_saved = annual_salary * percentage_saved / 12

portion_down_payment = total_cost * .25

months = 0 

while current_savings < portion_down_payment:
    months += 1
    current_savings = current_savings + (current_savings * r) + salary_saved
print("Number of months: ", months) 