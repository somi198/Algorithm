N = int(input())
F = list(map(int, input().split()))
F.sort()
answer = 0

for i in range(1, len(F)):
    start, end = 0, i-1
    j = -1
    
    while start <= end:
        mid = (start+end)//2
        
        if F[i]*0.9 <= F[mid] <= F[i]:
            j = mid
            end = mid-1
        else:
            start = mid+1
        
    if j >= 0: answer += i-j

print(answer)
