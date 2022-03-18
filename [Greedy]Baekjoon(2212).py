N = int(input())
K = int(input())
sensor = list(map(int, input().split()))
sensor.sort()

dist = []
for i in range(len(sensor)-1):
    dist.append(sensor[i+1]-sensor[i])
dist.sort(reverse=True)

print(sum(dist[K-1:]))