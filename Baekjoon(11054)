def LBS(N): # 가장 긴 바이토닉 부분 수열(Longest Bitonic subsequence)
    # 어떤 수 S(k)를 기준으로 S(1) < .. < S(k) > S(k+1) > .. > S(N)를 만족하는 가장 긴 부분수열의 길이를 구함
    left = [0]*N
    right = [0]*N
    DP = [1]*N

    for k in range(1, N):
        for i in range(k):
            if A[k] > A[i]:
                if left[k] <= left[i]+1:
                    left[k] = left[i]+1

    for k in range(N-2, -1, -1):
        for j in range(k, N):
            if A[k] > A[j]:
                if right[k] <= right[j]+1:
                    right[k] = right[j]+1

    for k in range(N):
        DP[k] += (left[k] + right[k])

    return max(DP)


N = int(input())
A = [int(x) for x in input().split()]
print(LBS(N))
