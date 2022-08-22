from collections import deque

def move_to_passenger(taxi):
    '''가장 가까운 승객으로 택시 이동'''
    global cost
    ty, tx = taxi
    
    min_dist = 10**9
    candidate = []
    visit = [[False]*N for _ in range(N)]
    dy, dx = [-1, 0, 0, 1], [0, -1, 1, 0] # 상좌우하
    
    Q = deque([(ty, tx, 0)])
    visit[ty][tx] = True
    
    while Q:
        y, x, distance = Q.popleft()
        
        if min_dist < distance: break
        elif graph[y][x] == 2:
            min_dist = distance
            candidate.append((y, x))
        
        for i in range(4):
            y_, x_ = y + dy[i], x + dx[i]
            
            if y_ < 0 or x_ < 0 or y_ >= N or x_ >= N: continue
            if graph[y_][x_] != 1 and not visit[y_][x_]:
                Q.append((y_, x_, distance+1))
                visit[y_][x_] = True
    
    if candidate: 
        candidate.sort(key=lambda x:(x[0], x[1]))
        cost -= min_dist
        return candidate[0]
    return -1
    

def move_to_destination(taxi, destination):
    '''승객을 태우고 목적지로 이동'''
    global cost
    ty, tx = taxi
    py, px = destination
    visit = [[False]*N for _ in range(N)]
    dy, dx = [-1, 0, 0, 1], [0, -1, 1, 0] # 상좌우하
    
    Q = deque([(ty, tx, 0)])
    visit[ty][tx] = True
    
    while Q:
        y, x, distance = Q.popleft()
        
        if (y, x) == (py, px):
            if cost < distance: return -1
            cost += distance
            return py, px
        
        for i in range(4):
            y_, x_ = y + dy[i], x + dx[i]
            
            if y_ < 0 or x_ < 0 or y_ >= N or x_ >= N: continue
            if graph[y_][x_] != 1 and not visit[y_][x_]:
                Q.append((y_, x_, distance+1))
                visit[y_][x_] = True   
    return -1        


N, M, cost = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
ty, tx = map(int, input().split())
taxi = (ty-1, tx-1)
passengers = {}
for _ in range(M):
    sy, sx, ex, ey = map(int, input().split())
    graph[sy-1][sx-1] = 2
    passengers[(sy-1, sx-1)] = (ex-1, ey-1)

for _ in range(M):
    # 1. 가장 가까운 승객까지 이동
    taxi = move_to_passenger(taxi)
    if cost < 0 or taxi == -1: break
    graph[taxi[0]][taxi[1]] = 0
    
    # 2. 승객을 태우고 목적지로 이동
    destination = passengers[taxi] # 현재 탑승한 승객의 최종 목적지
    taxi = move_to_destination(taxi, destination) 
    if taxi == -1: break

if cost < 0 or taxi == -1: print(-1)
else: print(cost)
