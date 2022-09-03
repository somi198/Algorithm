import sys
sys.setrecursionlimit(10000)

def dfs(point, land, visit):
    y, x = point
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]  # 시계방향(상,우,하,좌)

    for d in range(4):
        y_, x_ = y + dy[d], x + dx[d]
        if y_ < 0 or x_ < 0 or M <= y_ or N <= x_:
            continue
        if not visit[y_][x_] and land[y_][x_] == 1:
            visit[y_][x_] = True
            dfs((y_, x_), land, visit)

T = int(input())
for _ in range(T):
    ans = 0
    M, N, K = map(int, input().split())
    land = [[0]*N for _ in range(M)]
    visit = [[False]*N for _ in range(M)]
    for _ in range(K):
        y, x = map(int, input().split())
        land[y][x] = 1
    for y in range(M):
        for x in range(N):
            if not visit[y][x] and land[y][x] == 1:
                visit[y][x] = True
                dfs((y,x), land, visit)
                ans += 1
    print(ans)
