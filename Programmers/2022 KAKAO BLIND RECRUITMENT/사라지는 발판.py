from collections import deque

def solution(board, aloc, bloc):
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1] #상하좌우
    
    def dfs(y, x, ny, nx, cnt):
        win_info = []
        
        if board[ny][nx] == 0:
            return True, cnt
        if board[y][x] == 0:
            return False, cnt
        
        for i in range(4):
            y_, x_ = y+dy[i], x+dx[i]
            
            if y_ < 0 or x_ < 0 or y_ >= len(board) or x_ >= len(board[0]) or board[y_][x_] == 0:
                continue
            
            board[y][x] = 0
            next_win, next_play = dfs(ny, nx, y_, x_, cnt+1)
            win_info.append([not next_win, next_play])
            board[y][x] = 1
        
        if not win_info:
            return False, cnt
        elif any(info[0] for info in win_info):
            return True, min(info[1] for info in win_info if info[0])
        else:
            return False, max(info[1] for info in win_info)
        
        
    _, answer = dfs(aloc[0], aloc[1], bloc[0], bloc[1], 0)
    return answer