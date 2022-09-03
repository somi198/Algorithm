def knapsack(Things, K):
    n = len(Things)
    Things.sort(key=lambda x:x[1], reverse=True)
    Things.insert(0, (0,0))

    DP = [[0]*(K+1) for i in range(n+1)] # i번째 아이템까지 넣을 때, 무게 j이하로 만족하는 최대 가치

    for i in range(1, n+1):
        for j in range(i, K+1):
            if Things[i][0] <= j:
                DP[i][j] = max(DP[i-1][j-Things[i][0]]+Things[i][1], DP[i-1][j])
            else:
                DP[i][j] = DP[i-1][j]

    max_value = 0
    for i in range(1, n+1):
        max_value = max(max_value, max(DP[i]))

    return max_value

N, K = input().split()
N, K = int(N), int(K)

Things = []

for i in range(N):
    Things.append(tuple(map(int, input().split())))

print(knapsack(Things, K))

