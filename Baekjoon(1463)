N = int(input())

list = [0]*(N+1)
list[0] = 0
list[1] = 0

for i in range(2, N+1):
    if i%3 == 0:
        list[i] = min(list[int(i-1)], list[int(i/3)]) + 1
    elif i%2 == 0:
        list[i] = min(list[int(i-1)], list[int(i/2)]) + 1
    else:
        list[i] = list[i-1] + 1

print(list[N])
