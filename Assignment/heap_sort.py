def heap_sort(A):
    # global Hc, Hs
    n = len(A)

    make_heap(A)

    for k in range(len(A) - 1, -1, -1):
        A[0], A[k] = A[k], A[0]
        # Hs += 1
        n = n - 1
        heapify_down(A, 0, n)

def make_heap(A):
    n = len(A)
    for k in range(n-1, -1, -1):
        heapify_down(A, k, n)

def heapify_down(A, k, n):
    # global Hc, Hs
    while 2 * k + 1 < n:
        L, R = 2 * k + 1, 2 * k + 2
        if L < n and A[L] > A[k]:
            m = L
            # Hc += 1
        else:
            m = k
            # Hc += 1
        if R < n and A[R] > A[m]:
            m = R
            # Hc += 1
        if m != k:
            A[k], A[m] = A[m], A[k]
            k = m
            # Hs += 1
        else:
            break
