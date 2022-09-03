def wine_taste(podo):
    dp = [0]*len(podo) # i번째 포도주까지 고려했을 때 가장 많이 마신 포도주 양
    dp[0] = podo[0]

    for i in range(1, len(podo)):
        if i == 1:
            dp[i] = podo[i-1] + podo[i]
            continue
        dp[i] = max(dp[i-2]+podo[i], dp[i-3]+podo[i-1]+podo[i], dp[i-1])

    return dp[-1]

N = int(input())
podo = []
for _ in range(N):
    podo.append(int(input()))
print(wine_taste(podo))
