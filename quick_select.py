# 임의의 k번째로 작은 수 찾기 (가장 일반적인 selection 문제)

def quick_select(L, k):
    pivot = L[0]
    A, M, B = [], [], []
    for x in L:
        if x < pivot:
            A.append(x)
        elif x > pivot:
            B.append(x)
        else:
            M.append(x)

    if len(A) >= k:
        return quick_select(A, k)
    elif len(A) + len(M) < k:
        return quick_select(B, k-len(A)-len(M))
    else:
        return pivot

n, k = input().split()
n, k = int(n), int(k)
L = [0]*n
L = [int(x) for x in input().split()]
print(quick_select(L, k))

