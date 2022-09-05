import math
from collections import defaultdict

def solution(fees, records):
    answer = []
    parking = {}
    total = defaultdict(int)
    for record in records:
        time, car, info = record.split()
        h, m = map(int, time.split(':'))

        if info == 'IN':
            parking[car] = (h, m)
        else:
            In_h, In_m = parking[car]
            time = (h*60 + m) - (In_h*60 + In_m)
            total[car] += time
            parking.pop(car)
    
    for car in parking.keys():
        In_h, In_m = parking[car]
        time = (23*60 + 59) - (In_h*60 + In_m)
        total[car] += time

    total = sorted(total.items(), key=lambda x:x[0])

    for _, time in total:
        if time <= fees[0]:
            answer.append(fees[1])
        else:
            plus = math.ceil((time-fees[0])/fees[2])*fees[3]
            answer.append(fees[1]+plus)

    return answer