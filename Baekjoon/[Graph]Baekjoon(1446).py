import heapq
from collections import defaultdict

def dijkstra(D):
    '''D까지 이동할 때 최소 거리 반환'''
    Q = [(0, 0)]
    dist[0] = 0
    dist[D] = D

    while Q:
        cost, v = heapq.heappop(Q)
        if dist[v] < cost: continue
        
        # 1. v에서 모든 w로 갈 수 있는 경로의 거리 계산
        for w in dist.keys():
            if v >= w: continue
            if dist[w] > dist[v] + abs(w-v):
                dist[w] = dist[v] + abs(w-v)
                heapq.heappush(Q, (dist[w], w))
        
        # 2. v에서 w로 가는 지름길의 거리 계산  
        if v not in graph.keys(): continue  # v에서 갈 수 있는 지름길이 없다면 pass
        for w, cost in graph[v]:
            if dist[w] > dist[v] + cost:
                dist[w] = dist[v] + cost
                heapq.heappush(Q, (dist[w], w))
        
    return dist[D]

N, D = map(int, input().split())
dist = {}
graph = defaultdict(list)
for _ in range(N):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
    dist[start], dist[end] = float('inf'), float('inf')
 
print(dijkstra(D))
