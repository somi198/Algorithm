def LBS(A):
    ans = 0
    asc = [1]*N
    desc = [1]*N

    for k in range(N):
        for i in range(k):
            if A[k] > A[i]:
                asc[k] = max(asc[k], asc[i]+1)
            if A[N-k-1] > A[N-1-i]:
                desc[N-1-k] = max(desc[N-1-k], desc[N-1-i]+1)

    for i in range(N):
        ans = max(ans, asc[i]+desc[i])
    return ans-1

N = int(input())
A = list(map(int, input().split()))
print(LBS(A))
