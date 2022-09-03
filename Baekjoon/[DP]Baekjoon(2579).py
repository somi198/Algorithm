def other_solution(stairs): # 다른사람이 푼 솔루
    dp = [0]*N
    dp[0] = stairs[0]

    for i in range(1, N):
        if i == 1:
            dp[i] = max(dp[i-1]+stairs[i], stairs[i])
        else:
            dp[i] = max(dp[i-3]+stairs[i-1], dp[i-2]) + stairs[i] # max(전칸(+전전전칸 밟았을 때) or 전전칸 밟았을 때) + stairs[i] 현재칸

    return dp[-1]

def max_score(stairs):
    step1 = [0]*N
    step2 = [0]*N

    step1[0] = stairs[0]

    for i in range(1, N):
        if i == 1:
            step1[i] = stairs[i]
            step2[i] = step1[i-1] + stairs[i]
        else:
            step1[i] = max(step2[i-2], step1[i-2]) + stairs[i]
            step2[i] = step1[i-1] + stairs[i]

    return max(step1[-1], step2[-1])

N = int(input())
stairs = []
for _ in range(N):
    stairs.append(int(input()))
print(other_solution(stairs))
#print(max_score(stairs))
