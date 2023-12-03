""" my_list = []
for i in range(1, 10):
    my_list.append(i)
    print(my_list) """

""" lc = [i    for i in range(1, 10)]
print(lc) """

""" list_1 =[i for i in range(1, 20) if i % 2==0]
print(list_1) """

""" list_1=[]
for i in range (1, 20):
    if i % 2 == 0:
        list_1.append(i)
    print(list_1) """

""" rol_col = 4
matrix = [[(col + 1 + rol * rol_col) for col in range(4)] for rol in range(4)]
for m in matrix:
    print(m)

print(*matrix, sep="\n") """


number = int(input())
matrix = []

for i in range(number):
    matrix.append([])
    for col in range(number):
        matrix[i].append(col + 1 + i * number)
flat_list = []
for row in range(number):
    for col in range(number):
        flat_list.append(matrix[row][col])

print(*matrix, sep="\n")
print(flat_list) 


""" number = int(input())
matrix = [[(col + 1 + row * number)for col in range(number)] for row in range(number)]
print(*matrix, sep="\n") """