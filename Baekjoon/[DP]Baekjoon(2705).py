T = int(input())

for _ in range(T):
    n = int(input())
    
    dp = [0]*(n+1)
    dp[0], dp[1] = 1, 1
    
    for i in range(2, n+1):
        for j in range(i%2, i+1, 2):
            dp[i] += dp[(i-j)//2]
    
    print(dp[n])
