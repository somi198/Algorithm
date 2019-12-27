def LectureSelector(I):
    n = len(S)
    L = [I[0]]
    k = 0 #가장 최근에 뽑힌 강의 번호

    for i in range(1, n):
        if I[k][1] <= I[i][0]: #끝내는 시간 <= 시작하는 시간
            L.append(I[i])
            k = i

    return L

S = [int(x) for x in input().split()]
F = [int(y) for y in input().split()]
I = [(S[i],F[i]) for i in range(len(S))]
I.sort(key=lambda x: x[1])
print(LectureSelector(I))
