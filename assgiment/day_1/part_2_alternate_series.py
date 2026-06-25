n = int(input("Enter N: "))

low = 1
high = n

while low <= high:
    print(low, end=" ")
    if low != high:
        print(high, end=" ")
    low += 1
    high -= 1