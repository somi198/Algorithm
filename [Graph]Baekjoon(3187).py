from collections import deque

R, C = map(int, input().split())
grid = [list(input()) for _ in range(R)]
visit = [[False]*C for _ in range(R)]
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1] # 상하좌우
total_v, total_k = 0, 0

for root_y in range(R):
    for root_x in range(C):
        if grid[root_y][root_x] == '#' or visit[root_y][root_x]: continue
        
        v, k = 0, 0
        Q = deque([(root_y, root_x)])

        while Q:
            y, x = Q.popleft()
            
            if visit[y][x]: continue
            visit[y][x] = True
            
            if grid[y][x] == 'v': v += 1
            elif grid[y][x] == 'k': k += 1
            
            for i in range(4):
                y_, x_ = y + dy[i], x + dx[i]
                
                if y_ < 0 or x_ < 0 or y_ >= R or x_ >= C: continue
                if grid[y_][x_] != '#' and not visit[y_][x_]:
                    Q.append((y_, x_))
        
        if v >= k: total_v += v
        else: total_k += k

print(total_k, total_v)
