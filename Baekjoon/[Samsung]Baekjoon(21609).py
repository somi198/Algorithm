from collections import deque

def find_block_group():
    group = []
    rainbow = 0
    visit = [[False]*N for _ in range(N)]
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

    for i in range(N):
        for j in range(N):
            if grid[i][j] <= 0 or visit[i][j]: continue
            
            rainbow_ = 0
            group_ = [(i, j)] # standard block
            visit_ = [[False]*N for _ in range(N)]

            n = grid[i][j]
            Q = deque([(i, j)])
            visit[i][j] = True
            visit_[i][j] = True

            while Q:
                y, x = Q.popleft()

                for d in range(4):
                    y_, x_ = y+dy[d], x+dx[d]

                    if y_ < 0 or x_ < 0 or y_ >= N or x_ >= N: continue
                    elif visit_[y_][x_] or grid[y_][x_] not in (0, n): continue
                    
                    if grid[y_][x_] == 0: rainbow_ += 1
                    
                    visit[y_][x_] = True
                    visit_[y_][x_] = True
                    
                    Q.append((y_, x_))
                    group_.append((y_, x_))
            
            # compare
            if len(group_) > len(group):
                group = group_
                rainbow = rainbow_
            elif len(group_) == len(group):
                if rainbow_ > rainbow:
                    group = group_
                    rainbow = rainbow_
                elif rainbow_ == rainbow:
                    if group_[0][0] > group[0][0]:
                        group = group_
                    elif group_[0][0] == group[0][0]:
                        if group_[0][1] > group[0][1]:
                            group = group_

    return group

def remove_block_group(group):
    global score
    # caculate score
    score +=  len(group)**2

    # remove
    for i, j in group:
        grid[i][j] = -2

def gravity():
    for y in range(N-1, -1, -1):
        for x in range(N-1, -1, -1):
            if grid[y][x] < 0: continue
            
            y_, x_ = y, x
            while y_+1 < N and grid[y_+1][x_] == -2:
                y_ += 1
            
            grid[y][x], grid[y_][x_] = grid[y_][x_], grid[y][x]

def rotate():
    grid_ = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            grid_[N-1-j][i] = grid[i][j]

    return grid_


if __name__ == '__main__':

    score = 0
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    # 0. init block group
    block_group = find_block_group()

    while len(block_group) >= 2:
        # 1. remove block group & calculate score
        remove_block_group(block_group)
        # 2. gravity
        gravity()
        # 3. rotate
        grid = rotate()
        # 4. gravity
        gravity()
        # 5. find block group
        block_group = find_block_group()

    print(score)