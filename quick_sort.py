"""def quick_sort(A): #not-in-place
    if len(A)  <= 1:
        return A
    pivot = A[0]
    S, M, L = [], [], []
    for x in A:
        if x < pivot:
            S.append(x)
        elif x > pivot:
            L.append(x)
        else:
            M.append(x)
    return quick_sort(S)+M+quick_sort(L)
"""

def quick_sort2(A, first, last):
    if first >= last:
        return
    left, right = first+1, last
    pivot = A[first]
    while left <= right:
        while left <= last and A[left] < pivot:
            left += 1
        while right > first and A[right] >= pivot:
            right -= 1
        if left <= right:
            A[left], A[right] = A[right], A[first]
            left += 1
            right -= 1
    A[first], A[right] = A[right], A[first]
    quick_sort2(A, first, right-1)
    quick_sort2(A, right+1, last)
    return A

n = input()
A = [0]*n
A = input().split()
A = list(map(int, A))
#print(quick_sort(A))
print(quick_sort2(A, 0, len(A)))

