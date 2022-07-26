def dp(n):
    if n == 1: return 0
    if memo[n] != 0: return memo[n]
    
    memo[n] = dp(n-1)+1 
    if n%3 == 0:
        memo[n] = min(memo[n], dp(n//3)+1)
    if n%2 == 0:
        memo[n] = min(memo[n], dp(n//2)+1) 
    
    return memo[n]

N = int(input())
memo = [0]*(N+1)
print(dp(N))
