import copy

def solution(n, info):
    global max_diff, answer
    
    def calculate(): # calculate apeach score
        score = 0
        for i in range(11):
            if info[i] and info[i] >= possible[i]:
                score += 10-i
        return score
    
    def dfs(score, n, ryan):
        global max_diff, answer
        
        apeach = calculate()
        diff = ryan-apeach
        
        if diff > 0:
            candidate = possible.copy()
            
            if n > 0: candidate[-1] = n
            if max_diff < diff:
                max_diff = diff
                answer = candidate
            elif max_diff == diff:
                for i in range(10, -1, -1):
                    if candidate[i] < answer[i]: break
                    elif candidate[i] > answer[i]:            
                        answer = candidate
                        break
        
        for i in range(score, 11):
            if info[i] < n:
                possible[i] = info[i]+1
                dfs(i+1, n-(info[i]+1), ryan+(10-i))
                possible[i] = 0
     
        
    answer = [-1]
    max_diff = 0
    possible = [0]*11
    dfs(0, n, 0)    
    
    return answer