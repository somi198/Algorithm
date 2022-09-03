def max_sum(A):
    dp = [0]*len(A)
    dp[0] = A[0]

    for i in range(1, len(A)):
        dp[i] = max(dp[i-1]+A[i], A[i])

    return max(dp)

n = int(input())
A = list(map(int, input().split()))
print(max_sum(A))
