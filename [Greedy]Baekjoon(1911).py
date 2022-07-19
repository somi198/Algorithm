import math

N, L = map(int, input().split())
water = [tuple(map(int, input().split())) for _ in range(N)]
water.sort(key=lambda x:x[0])

answer = 0
last = -1

for start, end in water:
    if start < last:
        start = last
    
    interval = end-start
    answer += math.ceil(interval/L)
    
    if interval % L > 0: 
        last = end + L - interval%L
       
print(answer)
