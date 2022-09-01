import heapq
from collections import defaultdict

def dijkstra(n, info, graph):
    Q = []
    intensity = [float('inf')]*(n+1)
    
    for i in range(len(info)):
        if info[i] == 1: 
            Q.append((0, i)) # 출발 gate
            intensity[i] = 0
    
    while Q:
        cost, u = heapq.heappop(Q)
        
        if intensity[u] < cost: continue
        if info[u] == 2: continue
        
        for v, cost in graph[u]:
            if info[v] != 1 and intensity[v] > max(intensity[u], cost):
                intensity[v] = max(intensity[u], cost)
                heapq.heappush(Q, (intensity[v], v))
                
    return intensity

def solution(n, paths, gates, summits):
    info = [0]*(n+1)
    graph = defaultdict(list)
    answer = [n, 10000001]
    
    for a, b, cost in paths:
        graph[a].append((b, cost))
        graph[b].append((a, cost))
    
    for gate in gates: # 출입구: 1
        info[gate] = 1
    
    for summit in summits: # 산봉우리: 2
        info[summit] = 2
        
    summits.sort()
    intensity = dijkstra(n, info, graph)
    
    for summit in summits:
        if intensity[summit] < answer[1]:
            answer = [summit, intensity[summit]]
        
    return answer
