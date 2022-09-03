N = int(input())
meeting = [tuple(map(int, input().split())) for _ in range(N)]
meeting.sort(key=lambda x:(x[0], x[1]))
st = [meeting[0]]

for s, e in meeting[1:]:
    if s >= st[-1][1]:
        st.append((s, e))
    elif e < st[-1][1]:
        st.pop()
        st.append((s, e))

print(len(st))
