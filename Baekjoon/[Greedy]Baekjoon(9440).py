from collections import deque

cmd = input().split()

while cmd[0] != '0':
    N = int(cmd[0])
    number = deque(sorted(cmd[1:]))
    n1, n2 = '', ''
    
    while number:    
        zero = 0
        while not len(n1)*len(n2) and number:
            n = number.popleft()
            if n == '0': zero += 1
            elif not n1: n1 += n
            else: n2 += n
            
        number = deque(['0']*zero) + number
        if number: n1 += number.popleft()
        if number: n2 += number.popleft()
    
    print(int(n1)+int(n2))
    cmd = input().split()
