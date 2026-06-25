n = int(input("How many terms? "))

a = 1
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b