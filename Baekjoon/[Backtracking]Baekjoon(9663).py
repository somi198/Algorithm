def promising(row):
    for other_row in range(row):
        # 같은 열에 존재
        if queens[row] == queens[other_row]: return False
        # 대각선상에 존재
        if row-other_row == abs(queens[row]-queens[other_row]): return False

    return True

def dfs(row):
    answer = 0
    if row >= N: return 1
    
    for col in range(N):
        queens[row] = col

        if promising(row):
            answer += dfs(row+1)

    return answer

N = int(input())
queens = [0]*N

print(dfs(0))