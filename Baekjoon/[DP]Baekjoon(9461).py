# 파도반 수열

def P(N):
    if N <= 5:
        wave = [0]*5
    else:
        wave = [0]*N

    wave[0] = 1
    wave[1] = 1
    wave[2] = 1
    wave[3] = 2
    wave[4] = 2

    for k in range(5, len(wave)):
        wave[k] = wave[k - 5] + wave[k - 1]
    return wave[N-1]

T = int(input())
for _ in range(T):
    N = int(input())
    print(P(N))
