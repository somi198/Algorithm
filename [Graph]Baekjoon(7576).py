from collections import deque

def bfs(tomato, ripe_tomato):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]  # 시계방향(상,우,하,좌)
    count, day = 0, 0

    while True:
        close = deque() # 인접 토마토 큐
        while ripe_tomato:
            y, x = ripe_tomato.popleft()
            for d in range(4):
                y_, x_ = y + dy[d], x + dx[d]
                if y_ < 0 or x_ < 0 or N <= y_ or M <= x_:
                    continue
                if tomato[y_][x_] == 0:
                    count += 1          # 새로 익은 토마토의 개수
                    tomato[y_][x_] = 1
                    close.append((y_, x_))

        if not close: break     # 인접한 토마토가 없으면 break
        ripe_tomato = close
        day += 1
    return day, count

M, N = map(int, input().split())
tomato = []
for y in range(N):
    tomato.append(list(map(int, input().split())))

ripe_tomato = deque()
raw_tomato = 0  # 안 익은 토마토의 개수 
for y in range(N):
    for x in range(M):
        if tomato[y][x] == 1:
            ripe_tomato.append((y,x))
        elif tomato[y][x] == 0:
            raw_tomato += 1

day, count = bfs(tomato, ripe_tomato)
if raw_tomato == count: # 모든 토마토가 익었을 때 
    print(day)
else:                   # 익지 않은 토마토가 존재 
    print(-1)
