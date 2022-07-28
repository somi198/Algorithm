T = int(input())
for _ in range(T):
    N = int(input())
    DP = [[0]*(N+1) for _ in range(N+1)]
    
    for n in range(1, N+1):
        DP[n][n] = 1
        for k in range(n-1, 0, -1):
            DP[n][k] += DP[n-k][k+1] + DP[n][k+1]
    
    print(DP[N][1]%100999)
