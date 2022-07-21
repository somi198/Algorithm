import heapq

N = int(input())
lecture = [tuple(map(int, input().split())) for _ in range(N)]
lecture.sort(key=lambda x:x[0])
time = [0]

for s, t in lecture:
    if s >= time[0]: heapq.heappop(time)
    heapq.heappush(time, t)
print(len(time))
