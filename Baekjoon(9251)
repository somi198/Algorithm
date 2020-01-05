def LCS(List1, List2):
    DP = [[0]*(len(List2)) for i in range(len(List1))]

    for i in range(1, len(List1)):
        for j in range(1, len(List2)):
            if List1[i] == List2[j]:
                DP[i][j] = DP[i-1][j-1]+1
            else:
                DP[i][j] = max(DP[i-1][j], DP[i][j-1])

    return DP[len(List1)-1][len(List2)-1]

List1 = list(input())
List2 = list(input())
List1.insert(0,0)
List2.insert(0,0)

print(LCS(List1, List2))
