import heapq
from collections import defaultdict

def solution(n, s, a, b, fares):
    answer = float('inf')
    graph = defaultdict(list)
    
    for u, v, cost in fares:
        graph[u].append((v, cost))
        graph[v].append((u, cost))
    
    for i in range(n+1):
        Q = [(0, i)]
        dist = [float('inf')]*(n+1)
        dist[i] = 0
        
        while Q:
            cost, u = heapq.heappop(Q)
            
            if dist[u] < cost: 
                continue
            
            for v, cost in graph[u]:
                if dist[v] > dist[u]+cost:
                    dist[v] = dist[u]+cost
                    heapq.heappush(Q, (dist[v], v))
        
        answer = min(answer, dist[a]+dist[b]+dist[s])
    
    return answer