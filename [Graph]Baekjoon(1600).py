from collections import deque

K = int(input())
W, H = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(H)]
visit = [[[False]*W for _ in range(H)] for _ in range(K+1)]
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1] # 상,하,좌,우
hy, hx = [-2, -2, 2, 2, 1, 1, -1, -1], [-1, 1, -1, 1, -2, 2, -2, 2]

answer = -1
visit[0][0][0] = True
Q = deque([(0, 0, 0, 0)])

while Q:
    y, x, cnt, k = Q.popleft()
    
    if y == H-1 and x == W-1:
        answer = cnt
        break
    
    for i in range(4):
        y_, x_ = y + dy[i], x + dx[i]
        
        if y_ < 0 or x_ < 0 or y_ >= H or x_ >= W: continue
        if visit[k][y_][x_]: continue
        if graph[y_][x_] == 0:
            Q.append((y_, x_, cnt+1, k))
            visit[k][y_][x_] = True
    
    for i in range(8):
        y_, x_ = y + hy[i], x + hx[i]
        
        if y_ < 0 or x_ < 0 or y_ >= H or x_ >= W or k+1 > K: continue
        if visit[k+1][y_][x_]: continue
        if graph[y_][x_] == 0:
            Q.append((y_, x_, cnt+1, k+1))
            visit[k+1][y_][x_] = True
        
print(answer)
