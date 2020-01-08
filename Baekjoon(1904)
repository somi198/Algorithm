def zero_one(n):
    DP = [0]*(n+1)
    DP[1] = 1
    DP[2] = 2

    for k in range(3, n+1):
        DP[k] = (DP[k-1]+DP[k-2])%15746 # (n-1)자리 수에 1 붙인 수 + (n-2)자리 수에 00 붙인 수 

    return DP[n]

n = int(input())
print(zero_one(n))

