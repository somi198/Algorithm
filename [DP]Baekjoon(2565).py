def LIS(electric):
    dp = [1]*N

    for i in range(N):
        for j in range(i):
            if electric[i][1] > electric[j][1]:
                dp[i] = max(dp[i], dp[j]+1)

    return N-max(dp)

N = int(input())
electric = []
for _ in range(N):
    electric.append(list(map(int, input().split())))

electric.sort(key=lambda x:x[0])
print(LIS(electric))
