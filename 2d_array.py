rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
array = [[i * j for j in range(columns)] for i in range(rows)]
print("Generated Array:")
for row in array:
    print(row)
