import heapq

def solution(alp, cop, problems): # DP
    max_alp, max_cop = 0, 0
    
    for i in range(len(problems)):
        max_alp = max(max_alp, problems[i][0])
        max_cop = max(max_cop, problems[i][1])
        
    if max_alp <= alp: alp = max_alp
    if max_cop <= cop: cop = max_cop
    
    DP = [[float('inf')]*(max_cop+1) for _ in range(max_alp+1)]
    DP[alp][cop] = 0
    
    for a in range(alp, max_alp+1):
        for c in range(cop, max_cop+1):
            if a < max_alp: DP[a+1][c] = min(DP[a+1][c], DP[a][c]+1)
            if c < max_cop: DP[a][c+1] = min(DP[a][c+1], DP[a][c]+1)
            
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if a < alp_req or c < cop_req: continue
                next_alp = min(a+alp_rwd, max_alp)
                next_cop = min(c+cop_rwd, max_cop)
                DP[next_alp][next_cop] = min(DP[next_alp][next_cop], DP[a][c]+cost)
                
    return DP[-1][-1]

def dijkstra(alp, cop, problems):
    global max_alp, max_cop
    
    Q = [(0, alp, cop)]
    coding = [[float('inf')]*(max_cop+1) for _ in range(max_alp+1)]
    coding[alp][cop] = 0
    
    while Q:
        cost, alp, cop = heapq.heappop(Q)
        
        if coding[alp][cop] < cost: continue
        
        # 알고력 1 높이기
        if alp < max_alp and coding[alp+1][cop] > coding[alp][cop]+1:
            coding[alp+1][cop] = coding[alp][cop]+1
            heapq.heappush(Q, (coding[alp+1][cop], alp+1, cop))
        
        # 코딩력 1 높이기
        if cop < max_cop and coding[alp][cop+1] > coding[alp][cop]+1:
            coding[alp][cop+1] = coding[alp][cop]+1
            heapq.heappush(Q, (coding[alp][cop+1], alp, cop+1))
        
        # 문제풀어서 알고력, 코딩력 높이기
        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            if alp < alp_req or cop < cop_req: continue
            
            next_alp = min(alp+alp_rwd, max_alp)
            next_cop = min(cop+cop_rwd, max_cop)
            
            if coding[next_alp][next_cop] > coding[alp][cop] + cost:
                coding[next_alp][next_cop] = coding[alp][cop] + cost
                heapq.heappush(Q, (coding[next_alp][next_cop], next_alp, next_cop))
            
        
    return coding[-1][-1]

def solution2(alp, cop, problems): # 다익스트라 알고리즘
    global max_alp, max_cop
    
    max_alp, max_cop = 0, 0
    
    for i in range(len(problems)):
        max_alp = max(max_alp, problems[i][0])
        max_cop = max(max_cop, problems[i][1])
    
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    
    return dijkstra(alp, cop, problems)
