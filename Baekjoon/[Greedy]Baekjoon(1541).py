f = input()
split_sub = f.split('-')
ans = 0

for i, f_i in enumerate(split_sub):
    num = list(map(int, f_i.split('+')))
    if i == 0:
        ans += sum(num)
    else:
        ans -= sum(num)
print(ans)