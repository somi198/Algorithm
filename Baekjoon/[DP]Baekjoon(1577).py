from collections import defaultdict

N, M = map(int, input().split())
K = int(input())
repair = defaultdict(bool)
grid = [[0]*(N+1) for _ in range(M+1)]

for k in range(K):
    a, b, c, d = map(int, input().split())
    repair[(d, c, b, a)] = True
    repair[(b, a, d, c)] = True

for i in range(M+1):
    for j in range(N+1):
        if i == 0 and j == 0: grid[i][j] = 1
        elif i == 0:
            if not repair[(i, j, i, j-1)]: grid[i][j] += grid[i][j-1]
        elif j == 0:
            if not repair[(i, j, i-1, j)]: grid[i][j] += grid[i-1][j]
        elif repair[(i, j, i, j-1)] and repair[(i, j, i-1, j)]: continue
        elif repair[(i, j, i, j-1)]: grid[i][j] += grid[i-1][j]
        elif repair[(i, j, i-1, j)]: grid[i][j] += grid[i][j-1]
        else: grid[i][j] += grid[i-1][j] + grid[i][j-1]

print(grid[M][N])
