from collections import deque

N, M = map(int, input().split())
grid = [list(input()) for _ in range(N)]
y, x = map(int, input().split())
pr, pc = y-1, x-1

dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1] # 상우하좌
dir = ['U', 'R', 'D', 'L']
answer = [0, 0]


for i in range(4):
    Q = deque([(pr, pc, i, 0)])
    visit = [[0]*M for _ in range(N)]
    while Q:
        y, x, d, time = Q.popleft()
        
        if y < 0 or x < 0 or y >= N or x >= M or grid[y][x] == 'C':
            if answer[1] < time: 
                answer = [i, time]
            break
        elif grid[y][x] == '\\':
            if d%2 == 0: d = (d+3)%4
            else: d = (d+1)%4
        elif grid[y][x] == '/':
            if d%2 == 0: d = (d+1)%4
            else: d = (d+3)%4

        visit[y][x] += 1
        if visit[y][x] > 2:
            answer = [i, 'Voyager']
            break
        
        y_, x_ = y+dy[d], x+dx[d]
        Q.append((y_, x_, d, time+1))
    if answer[1] == 'Voyager':
        break
    
print(dir[answer[0]])
print(answer[1])
