m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

matrix = []

print("Enter matrix elements:")

for i in range(m):
    row = []
    for j in range(n):
        value = int(input())
        row.append(value)
    matrix.append(row)

# Create transpose
transpose = []

for j in range(n):
    row = []
    for i in range(m):
        row.append(matrix[i][j])
    transpose.append(row)

print("Original Matrix:")
print(matrix)

print("Transpose Matrix:")
print(transpose)
