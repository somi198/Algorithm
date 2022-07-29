N = int(input())
block = input()
dp = [0]*N

for i in range(N):
    for j in range(i):
        if block[i]+block[j] in ('BJ', 'OB', 'JO'):
            if j==0 or dp[j]:
                if dp[i]: dp[i] = min(dp[i], dp[j]+(i-j)**2)
                else: dp[i] = dp[j]+(i-j)**2

if dp[-1]: print(dp[-1])
else: print(-1) 
