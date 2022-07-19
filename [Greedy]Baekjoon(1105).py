L, R = input().split()
L_len, R_len = len(L), len(R)
answer = 0

same = False
for i in range(R_len):
    if L_len == R_len:
        if L[i] == R[i]:
            if L[i] == '8': answer += 1
            else: continue
        else: break

print(answer)
