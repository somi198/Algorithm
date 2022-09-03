import math

N, ATK = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]

start = 1
end = 123456*1000000*1000000
maxHP = start

while start <= end:
    mid = (start+end)//2
    atk = ATK
    curHP = mid

    for t, a, h in info:
        if t == 1: # 몬스터가 있을 경우
            atk_cnt = math.ceil(h / atk)      # 몬스터의 생명력이 다 깎일 때까지 공격한 횟수
            atked_cnt = math.ceil(curHP / a)  # 전사의 생명력이 다 깎일 때까지 공격당한 횟수

            if atk_cnt <= atked_cnt:
                curHP -= (atk_cnt-1) * a
            else:
                curHP = 0
                break

        else: # 포션이 있을 경우
            atk += a # 전사의 공격력 증가
            curHP += h # 전사의 생명력 증가
            if curHP >= mid: curHP = mid

    if curHP > 0:
        maxHP = mid
        end = mid-1
    else:
        start = mid+1

print(maxHP)
