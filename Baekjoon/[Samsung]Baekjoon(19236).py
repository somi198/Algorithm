import copy

def move_fish(shark, board):
    info = {}
    for y in range(4):
        for x in range(4):
            # fish exists
            if board[y][x] != 0:
                fish, fd = board[y][x]
                info[fish] = (y, x, fd)

    for fish in range(1, 17):
        if fish not in info.keys(): continue

        y, x, d = info[fish]

        for _ in range(8):
            y_, x_ = y+dy[d], x+dx[d]

            if y_ < 0 or x_ < 0 or y_ >= 4 or x_ >= 4 or shark == (y_, x_):
                d = (d+1)%8
                continue
            
            # fish exists
            if board[y_][x_] != 0:
                fish2, d2 = board[y_][x_]
                info[fish2] = (y, x, d2)
            
            board[y][x], board[y_][x_] = board[y_][x_], (fish, d)
            info[fish] = (y_, x_, d)
            break



def move_shark(shark, board, total):
    ans = 0
    sy, sx = shark

    if sy < 0 or sx < 0 or sy >= 4 or sx >= 4 or board[sy][sx]== 0:
        return total

    # eat fish
    fish, sd = board[sy][sx]
    board[sy][sx] = 0

    # move fish
    move_fish(shark, board)

    # move shark
    for i in range(1, 4):
        sy_, sx_ = sy + i*dy[sd], sx + i*dx[sd]
        board_ = copy.deepcopy(board)
        ans = max(ans, move_shark((sy_, sx_), board_, total+fish))
    
    return ans
        

board = [[0]*4 for _ in range(4)]
dir = {}

for y in range(4):
    info = list(map(int, input().split()))
    for i in range(0, 8, 2):
        a, b = info[i], info[i+1]
        board[y][i//2] = (a, b-1)

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]

shark = (0, 0)
print(move_shark(shark, board, 0))
