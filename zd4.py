n = int(input())
matrix = []
s1=0


for i in range(n):
    inputUser = list(map(int,input().split(', ')))
    matrix.append(inputUser)

for i in range(n):
    s1+=matrix[i][i]
print()
print(*matrix, sep='\n')
print()
print(s1)

