from collections import deque


def move(cur: tuple, d: int) -> tuple:
    '''
    주사위가 이동방향으로 한 칸 이동
    cur: (y, x) 현재 좌표
    d: direction (0:우, 1:하, 2:좌, 3:상)
    '''
    y, x = cur
    y_, x_ = y + dy[d], x + dx[d]

    if y_ < 0 or x_ < 0 or N <= y_ or M <= x_:
        d = (d + 2) % 4     # 이동할 칸이 없으면 반대 방향으로 이동
        y_, x_ = y + dy[d], x + dx[d]

    return (y_, x_), d


def change_dice(d: int, dice: list) -> list:
    '''
    주사위 전개도 값 변경
    d: direction (0:우, 1:하, 2:좌, 3:상)
    dice: 주사위 전개도 리스트
    '''
    if d % 2 == 0:  # 좌우 이동
        change_idx = [1, 2, 3, 5]
    elif d % 2 == 1:  # 상하 이동
        change_idx = [0, 2, 4, 5]

    temp = [0] * 4
    for i, idx in enumerate(change_idx):
        if d < 2:
            temp[(i + 1) % 4] = dice[idx]
        else:
            temp[(i - 1) % 4] = dice[idx]

    for i, idx in enumerate(change_idx):
        dice[idx] = temp[i]

    return dice


def change_dir(cur: tuple, d: int, dice: list) -> int:
    '''
    새로운 이동방향 결정
    cur: (y, x) 현재 좌표
    d: direction (0:우, 1:하, 2:좌, 3:상)
    dice: 주사위 전개도 리스트
    '''
    y, x = cur
    A = dice[5]
    B = info[y][x]

    if A > B:
        d = (d + 1) % 4
    elif A < B:
        d = (d - 1) % 4

    return d


def score(cur: tuple) -> int:
    '''
    점수 계산
    cur: (y, x) 현재 좌표
    '''
    y, x = cur
    Q = deque([(y, x)])
    B, C = info[y][x], 0
    visit = [[False] * M for _ in range(N)]
    visit[y][x] = True

    while Q:  # BFS
        y, x = Q.popleft()
        C += 1

        for d in range(4):
            y_, x_ = y + dy[d], x + dx[d]
            if y_ < 0 or x_ < 0 or N <= y_ or M <= x_:
                continue
            if not visit[y_][x_] and B == info[y_][x_]:
                Q.append((y_, x_))
                visit[y_][x_] = True

    return B * C


N, M, K = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]

dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]  # 시계방향
dice = [2, 4, 1, 3, 5, 6]
current, d = (0, 0), 0
ans = 0

for _ in range(K):
    current, d = move(current, d)     # 1. 주사위가 이동방향으로 한칸 움직임
    dice = change_dice(d, dice)       # 2. 주사위 전개도가 바뀜
    ans += score(current)             # 3. 주사위가 도착한 칸에 대한 점수를 획득
    d = change_dir(current, d, dice)  # 4. 이동방향 결정
print(ans)
