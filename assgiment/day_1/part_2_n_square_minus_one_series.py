n = int(input("Enter number of terms: "))

print(0, end=" ")

for i in range(2, n + 1):
    print(i * i - 1, end=" ")