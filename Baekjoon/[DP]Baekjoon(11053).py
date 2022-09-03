def LIS(A):
    dp = [1]*N

    for i in range(N):
        for j in range(i):
            if A[i] > A[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

N = int(input())
A = list(map(int, input().split()))

print(LIS(A))
