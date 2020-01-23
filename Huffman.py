from heapq import heappush, heappop

def Huffman(f):
    n = len(f)
    H = []
    for x in range(n):
        heappush(H, (f[x], '{0}'.format(x)))

    while len(H) > 1:
        a = heappop(H) # 가장 작은 빈도수 item
        b = heappop(H) # 두 번째로 작은 빈도수 item
        #print("a: ", a, "b: ", b)
        heappush(H, (a[0]+b[0], '({0}, {1})'.format(a[1], b[1])))

    tree_string = heappop(H)[1]
    return tree_string


f = [int(x) for x in input().split()]
print(Huffman(f))
