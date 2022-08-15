from collections import deque

N, M = map(int, input().split())
grid = [list(input()) for _ in range(N)]

answer = -1
y, x = (0, 0)
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]  # 상하좌우
visit = [[False]*M for _ in range(N)]  # 벽 안부수고 이동한 방문 기록
visit2 = [[False]*M for _ in range(N)] # 벽 부수고 이동한 방문 기록

q = deque([(y, x, 0, 1)])

while q:
    y, x, crush, cnt = q.popleft()

    if y == N-1 and x == M-1: 
        answer = cnt
        break
    
    if not crush and visit[y][x]: continue
    elif not crush and not visit[y][x]: visit[y][x] = True
    
    if crush and visit2[y][x]: continue
    elif crush and not visit2[y][x]: visit2[y][x] = True
    
    for i in range(4):
        y_, x_ = y + dy[i], x + dx[i]
        
        if y_ < 0 or x_ < 0 or y_ >= N or x_ >= M: continue
        if grid[y_][x_] == '0':
            if not crush and not visit[y_][x_]:
                q.append((y_, x_, crush, cnt+1))
            elif crush and not visit2[y_][x_]: 
                q.append((y_, x_, crush, cnt+1))
        elif grid[y_][x_] == '1' and not crush:
            q.append((y_, x_, crush+1, cnt+1))
        
print(answer)
