def N_M(i, N, M): # 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수
    global x

    if i == M:
        for j in range(M):
            print(arr[j], end=" ")
        print()
        return

    for j in range(N):
        if x[j] != 1: # 중복 없이
            x[j] = 1
            arr[i] = j+1
            N_M(i+1, N, M)
            x[j] = 0

N, M = list(map(int, input().split()))
x = [0]*N
arr = [0]*N
N_M(0, N, M)

