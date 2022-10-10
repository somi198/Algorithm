def solution(n, k, cmd):
    answer = ''
    remove = []
    table = {i: True for i in range(n)}
    
    for i in range(len(cmd)):
        c = cmd[i].split()
        
        if c[0] == 'U':
            cnt = 0
            while cnt < int(c[1]):
                k -= 1
                if table[k] == True:
                    cnt += 1
        elif c[0] == 'D':
            cnt = 0
            while cnt < int(c[1]):
                k += 1
                if table[k] == True:
                    cnt += 1       
        elif c[0] == 'C':
            k_ = k
            remove.append(k)
            table[k] = False
            
            
            while k+1 < n:
                k += 1
                if table[k]: break
            
            if not table[k]:
                while k_-1 >= 0:
                    k_ -= 1
                    if table[k_]: break
                k = k_
                
        elif c[0] == 'Z':
            z = remove.pop()
            table[z] = True
        
    for i in range(n):
        if table[i]: answer += 'O'
        else: answer += 'X' 
    
    return answer


def solution2(n, k, cmd):
    answer = ''
    remove = []
    table = {}
    info = [True]*n
    
    # init
    for i in range(-1, n+1):
        table[i] = [i-1, i+1]
    
    for i in range(len(cmd)):
        #print(cmd)
        #print(info)
        c = cmd[i].split()
        
        if c[0] == 'U':
            for _ in range(int(c[1])):
                k = table[k][0]
        elif c[0] == 'D':
            for _ in range(int(c[1])):
                k = table[k][1]
        elif c[0] == 'C':
            info[k] = False
            remove.append(k)
            prev, next = table[k]
            table[prev][1] = next
            table[next][0] = prev
            
            if next == n: k = prev
            else: k = next
            
        elif c[0] == 'Z':
            z = remove.pop()
            info[z] = True
            prev, next = table[z]
            table[prev][1] = z
            table[next][0] = z
            
    for i in range(n):
        if info[i]: answer += 'O'
        else: answer += 'X'
            
    return answer

n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
print(solution2(n, k, cmd))