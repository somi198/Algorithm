def solution(L, R):
    if len(L) != len(R):
       return 0
		
    answer = 0
    for i in range(len(R)):
        if L[i] == R[i]:
            if L[i] == '8': answer += 1
        else: break
    return answer

L, R = input().split()
print(solution(L, R))
