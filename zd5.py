n = int(input())
matrix = []
s2=0


for i in range(n):
    inputUser = list(map(int,input().split(', ')))
    matrix.append(inputUser)

for i in range(n):
    s2+=matrix[i][n-i-1]


print()
print(*matrix, sep='\n')
print()
print(s2)

