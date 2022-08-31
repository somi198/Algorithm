import heapq
from collections import defaultdict

def dijkstra(price:int)->bool:
    '''
    입력 받은 price 보다 큰 비용을 최대한 적게 사용하여 N에 도달하는 최소 비용 경로 계산
    return: N번까지 도달하는데 price보다 큰 비용을 K번 이하로 사용하고 왔는지?
    '''
    dist = [float('inf')]*(N+1)
    
    Q = [(0, 1)]
    dist[1] = 0
    
    while Q:
        cost, u = heapq.heappop(Q)
        
        if cost < dist[u]: continue
        
        for v, cost in graph[u]:
            if dist[v] > dist[u] + (cost > price):
                dist[v] = dist[u] + (cost > price)
                heapq.heappush(Q, (dist[v], v))
    
    return dist[N] <= K


N, P, K = map(int, input().split())
graph = defaultdict(list)

for _ in range(P):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))

start, end = 0, 1000000
answer = -1

while start <= end:
    mid = (start + end) // 2

    if dijkstra(mid): # mid 가격 이상으로 K번 이하 사용하여 N까지 도달
        answer = mid
        end = mid-1
    else:
        start = mid+1

print(answer)
