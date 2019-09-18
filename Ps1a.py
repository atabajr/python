#PERCENTAGE OF MY DREAM HOUSE
annual_salary=float(input("enter your salary:"))
portion_down_percentage=float(input("enter your portion down percentage"))
total_cost=float(input("enter your total cost:"))
month_salary=annual_salary/12
partial_save=(portion_down_percentage/100)*month_salary
print(partial_save)
