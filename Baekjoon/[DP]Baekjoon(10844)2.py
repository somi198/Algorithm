N = int(input())

list = [[0]*10 for x in range(N+1)]
list[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
sum = 0

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            list[i][j] = list[i-1][1]
        elif j == 9:
            list[i][j] = list[i-1][8]
        else:
            list[i][j] = list[i-1][j-1] + list[i-1][j+1]

for i in range(10):
    sum += list[N][i]

print(sum%1000000000)
