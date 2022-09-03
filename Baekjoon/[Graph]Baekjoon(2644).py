from collections import defaultdict, deque

n = int(input())
a, b = map(int, input().split())
m = int(input())
edge = defaultdict(list)
for _ in range(m):
    p, c = map(int, input().split())
    edge[p].append(c)
    edge[c].append(p)

Q = deque([(a, 0)])
visit = [False]*(n+1)
visit[a] = True
ans = -1

while Q:
    u, dist = Q.popleft()
    if u == b:
        ans = dist
        break

    for v in edge[u]:
        if not visit[v]:
            Q.append((v, dist+1))
            visit[v] = True
print(ans)
