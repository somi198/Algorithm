N = int(input())
block = input()
dp = [0]*N
dp[0] = 1

for i in range(N):
    for j in range(i):
        combi = block[i]+block[j]
        if combi in ('BJ', 'OB', 'JO') and dp[j]:
            if dp[i]: dp[i] = min(dp[i], dp[j]+(i-j)**2)
            else: dp[i] = dp[j]+(i-j)**2

print(dp[-1]-1)
