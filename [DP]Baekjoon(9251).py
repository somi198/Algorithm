def LCS(str1, str2):
    dp = [[0]*len(str2) for _ in range(len(str1))]

    for i in range(1, len(str1)):
        for j in range(1, len(str2)):
            if str1[i] == str2[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[-1][-1]

str1 = ' '+input()
str2 = ' '+input()
print(LCS(str1, str2))
