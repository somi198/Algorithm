W = int(input())
words = input().split()

S = [0]*len(words) #index로 끝나는 단어까지의 최소 페널티 배열
S[0] = (W-len(words[0]))**3

for i in range(1, len(words)):
    current_width = 0
    min_penalty = len(words)*(W**3)
    j = i

    while j>=0: 
        current_width += len(words[j]) + 1

        if j==0:
            current_penalty = (W-current_width+1)**3
        else:
            current_penalty = S[j-1] + (W-current_width+1)**3

        if current_width-1 <= W:
            if min_penalty > current_penalty:
                min_penalty = current_penalty
        else:
            break
        j = j-1

    S[i] = min_penalty

print(S[len(words)-1])
