a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Highest Number =", a)
elif b >= a and b >= c:
    print("Highest Number =", b)
else:
    print("Highest Number =", c)