import heapq
from collections import defaultdict

def dijkstra(X):
    dist = [float('inf')]*(N+1)
    
    Q = [(0, X)]
    dist[X] = 0
    
    while Q:
        d, v = heapq.heappop(Q)
        if dist[v] < d: continue
        
        for w in graph[v]:
            if dist[w] > dist[v]+1:
                dist[w] = dist[v]+1
                heapq.heappush(Q, (dist[w], w))          
    return dist

N, M, K, X = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

answer = False
dist = dijkstra(X)
for i in range(len(dist)): 
    if dist[i] == K: print(i); answer = True
if not answer: print(-1)
