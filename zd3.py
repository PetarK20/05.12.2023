num = int(input())
mtrix = []
for i in range(num):
    mtrix.append([])
    for j in range(num):
        mtrix[i].append(j + 1 + i * num)

sum1 = sum(mtrix[0][0:])
sum2 = sum(mtrix[1][0:])
sum3 = sum(mtrix[2][0:])


print(*mtrix, sep="\n")
print(sum1)
print(sum2)
print(sum3)