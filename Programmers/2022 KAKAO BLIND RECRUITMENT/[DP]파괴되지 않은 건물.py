def solution1(board, skill): # 완전탐색  O(T*N^2)-> 효율성테스트 x
    answer = 0
    
    for type, r1, c1, r2, c2, degree in skill:
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                if type == 1: # 공격
                    board[r][c] -= degree
                else:
                    board[r][c] += degree
    
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] > 0:
                answer += 1
    
    return answer


def solution2(board, skill): # IMOS법 O(N^2) -> 효율성테스트 o
    answer = 0
    imos = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]
    
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1: # 공격
            imos[r1][c1] -= degree
            imos[r1][c2+1] += degree
            imos[r2+1][c1] += degree
            imos[r2+1][c2+1] -= degree
        else: # 회복
            imos[r1][c1] += degree
            imos[r1][c2+1] -= degree
            imos[r2+1][c1] -= degree
            imos[r2+1][c2+1] += degree
    
    for r in range(len(board)):
        for c in range(1, len(board[0])):
            imos[r][c] += imos[r][c-1]
    
    for c in range(len(board[0])):
        for r in range(1, len(board)):
            imos[r][c] += imos[r-1][c]
                                
    for r in range(len(board)):
        for c in range(len(board[0])):
            board[r][c] += imos[r][c]
            if board[r][c] > 0:
                answer += 1
    
    return answer