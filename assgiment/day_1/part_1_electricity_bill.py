units = int(input("Enter Electricity Units: "))

if units <= 200:
    bill = 0

elif units <= 500:
    bill = (units - 200) * 2

elif units <= 900:
    bill = (300 * 2) + (units - 500) * 3

else:
    bill = (300 * 2) + (400 * 3) + (units - 900) * 5

print("Electricity Bill = ₹", bill)