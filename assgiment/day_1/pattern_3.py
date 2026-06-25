rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        if j % 2 == 1:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()