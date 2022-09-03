import heapq
from collections import defaultdict

def dijkstra(K):
    dist = [float('inf')]*(V+1)
    
    Q = [(0, K)]
    dist[K] = 0
    
    while Q:
        cost, u = heapq.heappop(Q)
        
        if dist[u] < cost: continue
        
        for v, cost in graph[u]:
            if dist[v] > dist[u] + cost:
                dist[v] = dist[u] + cost
                heapq.heappush(Q, (dist[v], v))
    return dist
    

V, E = map(int, input().split())
K = int(input())
graph = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    
distance = dijkstra(K)
for i in range(1, V+1):
    if distance[i] == float('inf'): print('INF')
    else: print(distance[i])
