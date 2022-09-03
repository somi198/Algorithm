def Triangle(List):
    DP = [0]*len(List)
    DP[0] = List[0]
    interval = 2
    k = 1

    while k < len(List):
        for i in range(k, k+interval):
            if i == k:
                DP[i] = DP[i-(interval-1)] + List[i]
            elif i == k+interval-1:
                DP[i] = DP[i-interval] + List[i]
            else:
                DP[i] = max(DP[i-(interval-1)], DP[i-interval]) + List[i]

        k = k + interval
        interval += 1

    return max(DP)

n = int(input())
List = []

for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(len(tmp)):
        List.append(tmp[j])

print(Triangle(List))
