num = int(input())
mtrix = []
for i in range(num):
    mtrix.append([])
    for j in range(num):
        mtrix[i].append(j + 1 + i * num)

for i in range(num):
    print(sum(mtrix[i]))


print(*mtrix, sep="\n")

