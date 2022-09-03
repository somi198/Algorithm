def converge_zero(A):
    A.sort()
    L, R = 0, len(A)-1
    min_L, min_R = 0, 0
    min_sum = 2000000000

    while L < R:
        if abs(A[L] + A[R]) < min_sum:
            min_sum = abs(A[L] + A[R])
            min_L, min_R = L, R

        if A[L] + A[R] <= 0:
            L += 1
        else:
            R -= 1

    return A[min_L], A[min_R]

n = int(input())
A = list(map(int, input().split()))
a1, a2 = converge_zero(A)
print(a1, a2)
