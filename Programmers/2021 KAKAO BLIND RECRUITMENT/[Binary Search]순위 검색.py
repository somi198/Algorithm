from collections import defaultdict

def solution(info, query):
    answer = []
    dic = defaultdict(list)

    for i in info:
        i = i.split()
        for lang in (i[0], '-'):
            for task in (i[1], '-'):
                for career in (i[2], '-'):
                    for food in (i[3], '-'):
                        dic[(lang, task, career, food)].append(int(i[4]))

    for key in dic:
        dic[key].sort()

    for q in query:
        q = q.split()
        lang, task, career, food = q[0], q[2], q[4], q[6]
        X = int(q[7])

        possible = dic[(lang, task, career, food)]
        left, right = 0, len(possible)-1
        q_ans = len(possible)

        while left <= right:
            mid = (left+right) // 2

            if possible[mid] < X:
                left = mid+1
            else:
                q_ans = mid
                right = mid-1
                
        answer.append(len(possible)-q_ans)

    return answer