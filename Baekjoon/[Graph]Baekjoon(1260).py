from collections import defaultdict, deque

N, M, V = map(int, input().split())
edge = defaultdict(list)
dfs, bfs = '', ''
for _ in range(M):
    u, v = map(int, input().split())
    edge[u].append(v)
    edge[v].append(u)

# DFS
visit = [False]*(N+1)
st = deque()
st.append(V)

while st:
    u = st.pop()
    edge[u].sort(reverse=True)
    for v in edge[u]:
        if not visit[v]:
            st.append(v)
    if not visit[u]:
        dfs += str(u)+' '
    visit[u] = True

# BFS
visit = [False]*(N+1)
Q = deque()
Q.append(V)

while Q:
    u = Q.popleft()
    edge[u].sort()
    for v in edge[u]:
        if not visit[v]:
            Q.append(v)
    if not visit[u]:
        bfs += str(u)+' '
    visit[u] = True

print(dfs.strip())
print(bfs.strip())
