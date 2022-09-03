import heapq
from collections import defaultdict

def dijkstra(start, end):
    dist = [float('inf')]*(N+1)
    
    Q = [(0, start)]
    dist[start] = 0
    
    while Q:
        cost, v = heapq.heappop(Q)
        
        if dist[v] < cost: continue
        
        for w, cost in bus[v]:
            if dist[w] > dist[v] + cost:
                dist[w] = dist[v] + cost
                heapq.heappush(Q, (dist[w], w))
    
    return dist[end]
        

N = int(input())
M = int(input())
bus = defaultdict(list)
for _ in range(M):
    a, b, cost = map(int, input().split())
    bus[a].append((b, cost)) 
s, e = map(int, input().split())

print(dijkstra(s, e))
