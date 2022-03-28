age = input("What is your current age? ")

age_int = int(age)

remaining_years = 90 - age_int
days_remaining = remaining_years * 365
weeks_remaining = remaining_years * 52
months_remaining = remaining_years * 12

print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")

