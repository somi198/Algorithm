def N_M3(i, N, M):

    if i == M:
        for j in range(M):
            print(arr[j], end=" ")
        print()
        return

    for j in range(N):
        arr[i] = j+1
        N_M3(i+1, N, M)

N, M = list(map(int, input().split()))
arr = [0]*M
N_M3(0, N, M)


