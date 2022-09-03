def N_M2(i, k, N, M): # i는 인덱스, k는 오름차순이 조건에 필요한 변

    if i == M:
        for j in range(M):
            print(arr[j], end=" ")
        print()
        return

    for j in range(k+1, N):
        if x[j] != 1:
            x[j] = 1
            arr[i] = j+1
            N_M2(i+1, j, N, M)
            x[j] = 0


N, M = list(map(int, input().split()))
x = [0]*N
arr = [0]*M
N_M2(0, -1, N, M)
