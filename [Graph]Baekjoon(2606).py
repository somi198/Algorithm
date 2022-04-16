from collections import defaultdict
def dfs(u, edge, visit):
    visit[u] = True
    for v in edge[u]:
        if not visit[v]:
            dfs(v, edge, visit)

N = int(input())
connect = int(input())
edge = defaultdict(list)
visit = [False]*(N+1)
for _ in range(connect):
    u, v = map(int, input().split())
    edge[u].append(v)
    edge[v].append(u)

dfs(1, edge, visit)
print(visit.count(True)-1)
