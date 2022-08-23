from collections import deque

def solution(fire, jihoon, visit):
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1] #상하좌우  
    
    Q = deque(fire)
    Q.append(jihoon)

    while Q:
        y, x, cnt, s = Q.popleft()
        
        for i in range(4):
            y_, x_ = y + dy[i], x + dx[i]
            
            if y_ < 0 or x_ < 0 or y_ >= R or x_ >= C:
                if s == 'j': return cnt+1
                continue
            if graph[y_][x_] != '#' and not visit[y_][x_]:
                Q.append((y_, x_, cnt+1, s))
                visit[y_][x_] = True
                
    return 'IMPOSSIBLE'

R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]
visit = [[False]*C for _ in range(R)]
fire = []

for y in range(R):
    for x in range(C):
        if graph[y][x] == 'J':
            J = (y, x, 0, 'j')
            visit[y][x] = True
        elif graph[y][x] == 'F':
            fire.append((y, x, 0, 'f'))
            visit[y][x] = True

print(solution(fire, J, visit))
