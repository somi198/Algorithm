# a의 n승 계산하기

def power1(a, n): #선형 재귀로 호출 작성하기
    p=1
    for x in range(n):
       p = p *a
    return p

def power2(a, n): #이중 재귀로 호출하기
    if n == 0:
        return 1
    x = power2(a,n//2)
    if n%2 == 0:
        return x*x
    else:
        return x*x*a


a, n = input().split()
a, n = int(a), int(n)
print("power1: ",power1(a,n))
print("power2: ", power2(a, n))
