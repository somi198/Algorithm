def check_num(y, x):
    dic = {
        0: [[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]],
        1: [[0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]],
        2: [[1, 1, 1], [0, 0, 1], [1, 1, 1], [1, 0, 0], [1, 1, 1]],
        3: [[1, 1, 1], [0, 0, 1], [1, 1, 1], [0, 0, 1], [1, 1, 1]],
        4: [[1, 0, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [0, 0, 1]],
        5: [[1, 1, 1], [1, 0, 0], [1, 1, 1], [0, 0, 1], [1, 1, 1]],
        6: [[1, 1, 1], [1, 0, 0], [1, 1, 1], [1, 0, 1], [1, 1, 1]],
        7: [[1, 1, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1]],
        8: [[1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 1, 1]],
        9: [[1, 1, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [1, 1, 1]]
    }
    
    for n in range(10):
        Check = True
        num = dic[n]
        for r in range(5):
            for c in range(3):
                if num[r][c] != grid[y+r][x+c]:
                    Check = False
                    break
            if not Check: break  
        if Check: return n
    return -1
        
    
N = int(input())
signal = input()

answer = ''
row, col = 5, N//5
grid = [[0]*(col+3) for _ in range(row)]

for i in range(N):
    if signal[i] == '#':
        r, c = i//col, i%col
        grid[r][c] = 1

for r in range(row):
    grid[r] = [0] + grid[r]
    
c = 0
while c < col:
    num = check_num(0, c)
    if num >= 0: answer += str(num)
    c += 1
print(answer)
