def merge_two_sorted_list(A, first, last):
    # global Mc, Ms
    m = (first + last) // 2
    i, j = first, m + 1
    B = []
    while i <= m and j <= last:
        if A[i] <= A[j]:
            B.append(A[i])
            i += 1
            # Mc += 1
        else:
            B.append(A[j])
            j += 1
            # Mc += 1
    for k in range(i, m + 1):
        B.append(A[k])
    for k in range(j, last + 1):
        B.append(A[k])
    for i in range(first, last + 1):
        A[i] = B[i - first]


def merge_sort(A, first, last):
    # global Mc, Ms
    if first >= last:
        return
    m = (first + last) // 2
    merge_sort(A, first, m)
    merge_sort(A, m + 1, last)
    merge_two_sorted_list(A, first, last)
