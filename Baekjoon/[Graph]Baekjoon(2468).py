import sys
sys.setrecursionlimit(10000)

def dfs(point, rain, visit):
    y, x = point
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]  # 시계방향(상,우,하,좌)

    for d in range(4):
        y_, x_ = y + dy[d], x + dx[d]
        if y_ < 0 or x_ < 0 or N <= y_ or N <= x_:
            continue
        if not visit[y_][x_] and rain[y_][x_] > 0:
            visit[y_][x_] = True
            dfs((y_, x_), rain, visit)

N = int(input())
rain = []
for _ in range(N):
    rain.append(list(map(int, input().split())))

ans = 1
while True:
    safe = 0
    for i in range(N):
        for j in range(N):
            if rain[i][j] > 0:
                rain[i][j] -= 1

    visit = [[False] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if not visit[y][x] and rain[y][x] > 0:
                visit[y][x] = True
                dfs((y,x), rain, visit)
                safe += 1
    if not safe:
        break
    ans = max(ans, safe)
print(ans)
