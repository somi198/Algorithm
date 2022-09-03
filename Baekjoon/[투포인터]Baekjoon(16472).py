from collections import defaultdict

N = int(input())
S = input()

start, end = 0, 0
alphabet = defaultdict(int)
answer = 0
cnt = 0

while end < len(S):
    if alphabet[S[end]] <= 0:
        if cnt < N:
            cnt += 1
            alphabet[S[end]] += 1
            end += 1
        else:
            answer = max(answer, end - start)
            alphabet[S[start]] -= 1
            if alphabet[S[start]] <= 0:
                cnt -= 1
            start += 1
    else:
        alphabet[S[end]] += 1
        end += 1

if cnt <= N:
    answer = max(answer, end-start)
print(answer)
