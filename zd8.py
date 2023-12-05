number = int(input())
matrix = []
search_sym = input()
find_sym = False
for i in range(number):
    matrix.append([input()])
for i in range(number):
    for j in range(number):
        current_sym = matrix[i][j]
        if current_sym == search_sym:
            print(f"({i}, {j})")
            find_sym = True
            break
        else:
            print(f'{search_sym} not in matrix')
            find_sym = False
