def covid(waiting, P):
    for i in range(len(P)):
        # current
        cy, cx = P[i]
        for j in range(i+1, len(P)):
            # next
            ny, nx = P[j]
            # difference
            dy, dx = ny-cy, nx-cx
            distance = abs(dy) + abs(dx)

            if distance == 1: return 0
            elif distance == 2:
                if abs(dy) == 1 and abs(dx) == 1:
                    if waiting[cy+dy][cx] + waiting[cy][cx+dx] != 'XX': return 0
                else:
                    if waiting[cy+dy//2][cx+dx//2] != 'X': return 0
    return 1
    

def solution(places):
    answer = []
    
    for place in places:
        P = []
        waiting = [list(info) for info in place]
        
        for y in range(5):
            for x in range(5):
                if waiting[y][x] == 'P': P.append((y, x))
                    
        answer.append(covid(waiting, P))
        
    return answer