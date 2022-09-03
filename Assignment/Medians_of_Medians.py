# Medians-of-Medians 알고리즘

def five_median(L):
    L.sort()
    return L[len(L)//2]

def Median_of_Medians(L, k):

    if len(L) == 1:
        return L[0]

    A, B, M, medians=[], [], [], []
    i=0
    while i+4 < len(L):
        medians.append(five_median(L[i:i+5]))
        i = i+5
    if i<len(L) and i+4 >= len(L):
        medians.append(five_median(L[i:]))

    MoM = Median_of_Medians(medians, (len(medians)+1)//2)

    for x in L:
        if MoM > x:
            A.append(x)
        elif MoM < x:
            B.append(x)
        else:
            M.append(x)

    if len(A) >= k:
        return Median_of_Medians(A, k)
    elif len(A)+len(M) < k:
        return Median_of_Medians(B, k-len(A)-len(M))
    else:
        return MoM

n, k = input().split()
n, k = int(n), int(k)
L = [0]*n
L = [int(x) for x in input().split()]
print(Median_of_Medians(L, k))
