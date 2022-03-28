height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

w_int = int(weight)
h_float= float(height)

bmi= w_int/h_float**2
bmi_int = int(bmi)

print(bmi_int)