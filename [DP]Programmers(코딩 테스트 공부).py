def solution(alp, cop, problems):
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
