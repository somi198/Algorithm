import heapq

N = int(input())
X = [int(input()) for _ in range(N)]

heap = []

for x in X:
    if x == 0:
        if not heap: print(0)
        else: print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)
