n = int(input())
matrix = []

for _ in range(n):
    UserInput = list(map(int, input().split(', ')))
    matrix.append(UserInput)


diagonal_sum = 0
for i in range(n):
    diagonal_sum += matrix[i][i]

print(diagonal_sum)
