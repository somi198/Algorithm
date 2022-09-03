# selection (선택문제)
# 가장 큰 수와 가장 작은 수 찾기

"""def findMaxMin(A, n): #T(n) = 2n - 3(총 비교횟수)
    currentMin = 0
    currentMax = 0
    for i in range(1, n):
        if A[currentMin] > A[i]:
            currentMin = i
    currentMin = A.pop(currentMin)
    for j in range(1, n-1):
        if A[currentMax] < A[j]:
            currentMax = j
    currentMax = A[currentMax]
    return currentMin, currentMax"""

def findMax(A, B): 
    if len(A) == 1:
        return A[0]
    elif len(A) == 2:
        B.append(min(A[0], A[1]))
        return max(A[0], A[1])
    else:
       return  max(findMax(A[:len(A)//2], B), findMax(A[len(A)//2:], B))

def findMaxMin(A, n): #T(n) = 3n/2 - 3(총 비교횟수)
    Minlist = []

    Max = findMax(A, Minlist)

    Min = Minlist[0]
    for i in range(len(Minlist)):
        if Min > Minlist[i]:
            Min = Minlist[i]

    return Min, Max


A = [int(x) for x in input().split()]
Min, Max = findMaxMin(A, len(A))
print("Min: ", Min, " Max: ", Max)




