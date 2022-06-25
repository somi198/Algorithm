N = int(input())
A = list(map(int, input().split()))
A.sort()
answer = 0

for i in range(len(A)):
    c = A[i]
    start, end = 0, len(A)-1

    while start < end:
        if start == i: start += 1
        elif end == i: end -= 1

        a, b = A[start], A[end]

        if a + b < c:
            start += 1
        elif a + b > c:
            end -= 1
        else:
            answer += 1
            break

    #print(f'c = {c}, answer = {answer}')
print(answer)
