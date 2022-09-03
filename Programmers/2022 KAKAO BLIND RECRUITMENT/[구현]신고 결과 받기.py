from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    info = defaultdict(list)
    blocked = defaultdict(int)
    
    for r in report:
        user_a, user_b = r.split()
        if user_b not in info[user_a]:
            info[user_a].append(user_b)
            blocked[user_b] += 1
        
    for u_id in id_list:
        cnt = 0
        for reported_user in info[u_id]:
            if blocked[reported_user] >= k:
                cnt += 1
        answer.append(cnt)
    return answer