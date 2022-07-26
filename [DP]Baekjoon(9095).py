def dp(n):
    if n == 1: return 1
    if n == 2: return 2
    if n == 3: return 4
    if memo[n] != 0: return memo[n]
    
    memo[n] = dp(n-1) + dp(n-2) + dp(n-3)
    return memo[n]
    
T = int(input())
memo = [0]*(11)
for _ in range(T): print(dp(int(input())))
