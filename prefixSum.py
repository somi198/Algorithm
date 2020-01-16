import time, random


def prefixSum1(X, n):  # O(n^2)
    S = [0] * n
    for i in range(n):
        for j in range(i + 1):
            S[i] = S[i] + X[j]


def prefixSum2(X, n):  # O(n)
    S = [0] * n
    for i in range(1, n):
        S[i] = S[i - 1] + X[i]


random.seed()  # random 함수 초기화
n = int(input())
X = [0] * n
for i in range(n):
    X[i] = random.randint(-999, 999)  # 리스트 X를 randint를 호출하여 n개의 랜덤한 숫자로 채움
before = time.clock()
prefixSum1(X, n)  # prefixSum1 호출
after = time.clock()
print("prefixSum1: ", after - before)
before = time.clock()
prefixSum2(X, n)  # prefixSum2 호출
after = time.clock()
print("prefixSum2: ", after - before)
# 두 함수의 수행시간 출력
