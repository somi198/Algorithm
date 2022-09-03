N = int(input())
while N:
    P = [int(input()) for _ in range(N)]
    dp = [-10000]*N
    answer = -10000
    
    for i in range(N):
        dp[i] = max(P[i], P[i]+dp[i-1])
        answer = max(dp[i], answer)
    
    print(answer)
    N = int(input())
