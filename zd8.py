n = int(input())
matrix = []
for _ in range(n):
    UserInput = list(input())
    matrix.append(UserInput)
    flat_list = sum(matrix, [])

target_symbol = input()

reda = 0
while reda < n:
    if target_symbol in flat_list:
        for i in flat_list:
            index1 = UserInput.index(target_symbol)
        print(f"({index1}, {matrix.index(target_symbol)})")
        break
    reda += 1
else:
    print(f"{target_symbol} does not exist in matrix!")
