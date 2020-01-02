def upStairs(cost, n):
    DP = [[0]*(n+1) for i in range(n+1)] #DP[i][j] : i에서 j로 갈 때 얻는 누적 점수
    DP[0][1] = cost[1]
    DP[0][2] = cost[2]
    DP[1][2] = DP[0][1]+cost[2]
    DP[1][3] = DP[0][1]+cost[3]

    for k in range(2, n):
        DP[k][k+1] = DP[k-2][k]+cost[k+1] 
        if k < n-1:
            DP[k][k+2] = max(DP[k-2][k]+cost[k+2], DP[k-1][k]+cost[k+2])

    max_score = 0
    for i in range(n+1):
        if max_score < DP[i][n]:
            max_score = DP[i][n]

    return max_score

n = int(input())
cost = []
cost.append(0)

for i in range(1, n+1):
    cost.append(int(input()))

print(upStairs(cost, n))
