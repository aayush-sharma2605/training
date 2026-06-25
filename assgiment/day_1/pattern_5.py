rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    odd = 1
    for j in range(i):
        print(odd, end=" ")
        odd += 2
    print()