income = float(input("Enter Annual Income: "))

if income > 400000:
    tax = income * 0.30
elif income > 300000:
    tax = income * 0.20
elif income > 200000:
    tax = income * 0.10
else:
    tax = 0

print("Tax =", tax)