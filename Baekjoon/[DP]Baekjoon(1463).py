def dp(n):  # other solution (N까지 모든 리스트를 확인하지 않고 수를 나누면서 꼭 필요한 값만 확인)
    if n in cache:
        return cache[n]

    # 핵심 코드
    cnt = 1 + min(dp(n // 3) + n % 3, dp(n // 2) + n % 2)
    # 몫에다가 나머지를 더해주는 이유는 n이 11일 때 3으로 나눈 나머지가 2이므로 11에 -1을 두 번 뺴준 연산을 더하는 것!
    cache[n] = cnt
    return cnt

def make_one(N):
    dp = [0]*(N+1)

    for n in range(2,N+1):

        dp[n] = dp[n - 1] + 1
        if n % 3 == 0:
            dp[n] = min(dp[n], dp[n//3]+1)
        if n % 2 == 0:
            dp[n] = min(dp[n], dp[n//2]+1)

    return dp[N]

N = int(input())
cache = {1: 0, 2: 1}
print(make_one(N))
print(dp(N))
