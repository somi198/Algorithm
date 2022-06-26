M, N, L = map(int, input().split())
shoot = list(map(int, input().split()))
shoot.sort()
animal = [tuple(map(int, input().split())) for _ in range(N)]
answer = 0

for a, b in animal:
    start, end = 0, len(shoot)-1
    x = end

    while start <= end:
        mid = (start + end) // 2

        if shoot[mid] < a:
            start = mid + 1
        else:
            x = mid
            end = mid - 1

    if abs(shoot[x] - a) + b <= L or abs(shoot[x-1] - a) + b <= L:
        answer += 1

print(answer)
