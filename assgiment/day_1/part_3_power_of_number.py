base = int(input("Enter base: "))
power = int(input("Enter exponent: "))

result = 1

for i in range(power):
    result *= base

print("Answer =", result)