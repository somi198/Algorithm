def RGB(House):
    DP = [[1000]*3 for i in range(House)]
    DP[0][0] = cost[0][0]
    DP[0][1] = cost[0][1]
    DP[0][2] = cost[0][2]

    for k in range(1, House):
        for i in range(3):
            if i == 0:
                DP[k][i] = min(DP[k-1][1]+cost[k][i], DP[k-1][2]+cost[k][i])
            elif i == 1:
                DP[k][i] = min(DP[k-1][0]+cost[k][i], DP[k-1][2]+cost[k][i])
            else:
                DP[k][i] = min(DP[k-1][0]+cost[k][i], DP[k-1][1]+cost[k][i])

    return min(DP[House-1])

House = int(input())
cost = []

for i in range(House):
    cost.append(list(map(int, input().split())))

print(RGB(House))
