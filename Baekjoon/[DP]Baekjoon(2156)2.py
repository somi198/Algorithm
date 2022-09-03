n = int(input())
podo = []
list = [0]*n

for i in range(n):
    podo.append(int(input()))

for j in range(n):
    if j == 0:
        list[j] = podo[0]
    elif j == 1:
        list[j] = podo[0] + podo[1]
    elif j == 2:
        list[j] = max(list[j-1], podo[j]+podo[j-2], podo[j]+podo[j-1])
    else:
        list[j] = max(list[j-1], list[j-2]+podo[j], podo[j]+podo[j-1]+list[j-3])

print(list[n-1])
