import math

def is_prime_number(n):
    if n == 1: return False

    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0: return False
    return True

def solution(n, k):
    answer = 0
    
    # k진수로 변환
    new_n = ''
    while n > 0:
        new_n = f'{n%k}' + new_n
        n = n//k
    
    # prime number count
    new_n = new_n.split('0')
    for n in new_n:
        if n and is_prime_number(int(n)):
            answer += 1
    
    return answer