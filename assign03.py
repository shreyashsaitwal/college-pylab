# Floyd's triangle is a right-angled triangular array of natural numbers as
# shown below:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# Write a python program to print the Floyd’s triangle

inp = int(input("Enter the number of rows: "))

count = 1
for i in range(inp):
    for j in range(i + 1):
        print(count, end=" ")
        count += 1
    print()
