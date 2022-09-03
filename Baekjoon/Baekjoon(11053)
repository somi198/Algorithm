def LIS_DP(seq):
    DP = [0]*len(seq)
    DP[0] = 1

    for k in range(1, len(seq)):
        for i in range(k):
            if seq[k] > seq[i]:
                if DP[k] < DP[i]+1:
                    DP[k] = DP[i]+1
                else:
                    DP[k] = DP[k]
            else:
                if DP[k] > 1:
                    DP[k] = DP[k]
                else:
                    DP[k] = 1

    lis = max(DP)
    return lis

n = input()
seq = [int(x) for x in input().split()]
lis = LIS_DP(seq)
print(lis)
