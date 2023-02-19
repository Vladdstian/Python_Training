print("Welcome to the tip calculator.\n")
total_bill = float(input("What was the total bill? $"))
percentage = float(input("What percentage would you like to give? 10, 12, or 15%? "))
people = int(input("How many people to split the bill? "))
print()
total_with_percentage = total_bill + percentage/100*total_bill
total_per_person = total_with_percentage / people
print(f"Each person should pay: ${total_per_person:.2f}")
