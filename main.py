print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10,12 or 15 "))
no_of_people = int(input("How many people to split the bill? "))

#tip percentage = tip/100
#bill with tip = tip percentage * total bill

bill_with_tip = tip / 100 * total_bill + total_bill
bill_per_person = bill_with_tip / no_of_people
total_bill_person= round(bill_per_person, 2)
print(total_bill_person)