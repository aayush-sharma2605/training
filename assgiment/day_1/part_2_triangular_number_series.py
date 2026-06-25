n = int(input("Enter number of terms: "))

sum = 0

for i in range(1, n + 1):
    sum += i
    print(sum, end=" ")