n = int(input())
matrix = []

for _ in range(n):
    UserInput = list(map(int, input().split(', ')))
    matrix.append(UserInput)


diagonal_sum = 0
for i in range(n):
    for j in range(i + 1):
        diagonal_sum += matrix[i][j]

print(diagonal_sum)
