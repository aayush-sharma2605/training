n = int(input("Enter number of terms: "))

for i in range(n):
    if i % 2 == 0:
        print(1, end=" ")
    else:
        print(0, end=" ")