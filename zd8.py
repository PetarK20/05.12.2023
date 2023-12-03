n = int(input())
matrix = []

for _ in range(n):
    UserInput = list(map(int, input().split(', ')))
    matrix.append(UserInput)
print(matrix)