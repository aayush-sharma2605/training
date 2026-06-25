rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()