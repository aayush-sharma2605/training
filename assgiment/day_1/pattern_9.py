rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    if i == 2:
        for j in range(3):
            print(1, end=" ")
    else:
        print(1, end="")
    print()