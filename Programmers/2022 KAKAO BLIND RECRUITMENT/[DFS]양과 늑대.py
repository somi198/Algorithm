def solution(info, edges):
    global answer
    answer = 0
    visit = [False]*len(info)
    visit[0] = True

    def dfs(sheep, wolf):
        global answer
        if sheep > wolf:
            answer = max(answer, sheep)
        else: return

        for parent, child in edges:
            isWolf = info[child]
            if visit[parent] and not visit[child]:
                visit[child] = True
                dfs(sheep+(isWolf==0), wolf+(isWolf==1))
                visit[child] = False

    dfs(1, 0)               
    return answer

info = [0,1,0,1,1,0,1,0,0,1,0]
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
print(solution(info, edges))