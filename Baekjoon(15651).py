def N_M3(i, N, M):

    if i == M:
        print()
        return

    for j in range(N):
        print(j+1, end=" ")
        N_M3(i+1, N, M)

N, M = list(map(int, input().split()))
x = [0]*N
arr = [0]*M
N_M3(0, N, M)

