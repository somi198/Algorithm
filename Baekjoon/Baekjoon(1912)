def maxsum(A, n):
    DP = [0]*n
    DP[0] = A[0]

    for i in range(n):
        DP[i] = max(DP[i-1]+A[i], A[i])

    return max(DP)

n = int(input())
A = [int(x) for x in input().split()]

print(maxsum(A, n))
