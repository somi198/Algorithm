def strToSecond(time):
    h, m, s = map(int, time.split(':'))
    return 60*60*h + 60*m + s

def secondToStr(time):
    s = time%60
    m = (time//60)%60
    h = (time//60)//60
    return f'{h:02d}:{m:02d}:{s:02d}'

def solution(play_time, adv_time, logs):
    answer = 0
    play_time = strToSecond(play_time)
    adv_time = strToSecond(adv_time)
    ad = [0]*(play_time+1)
        
    for log in logs:
        t1, t2 = log.split('-')
        t1, t2 = strToSecond(t1), strToSecond(t2)
        ad[t1] += 1
        ad[t2] -= 1
    
    for i in range(1, len(ad)):
        ad[i] += ad[i-1]
    
    sum = 0
    for t in range(adv_time):
        sum += ad[t]
    
    max_sum = sum
    start = 0
    for end in range(adv_time, play_time+1):
        sum += ad[end]
        sum -= ad[start]
        start += 1
        
        if max_sum < sum:
            max_sum = sum
            answer = start
    
    return secondToStr(answer)