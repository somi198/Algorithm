def two_pointer(A, x):
    A.sort()
    left, right =  0, len(A)-1
    count = 0

    while left < right:
        if A[left] + A[right] < x:
            left += 1
        elif A[left] + A[right] > x:
            right -= 1
        else:
            count += 1
            left += 1

    return count

n = int(input())
A = list(map(int, input().split()))
x = int(input())
print(two_pointer(A, x))
