"""
20221122

2022 KAKAO BLIND RECRUITMENT

3. 주차요금계산
- Problem : 
    https://school.programmers.co.kr/learn/courses/30/lessons/92341  

주의할점
    풀긴했으나 while문이 좀 마음에 안듦
    While문 부분 (IN OUT 시간 계산하는 파트) Refernece 참고
      - record루프
        - 차량번호 별로 In, out status를 조건문으로 바로 time계산하기
        - 그리고 해당 차량번호의 마지막 Status 기록
      - 마지막 상태가 IN이면 1439분(23:59)에서 뺀 만큼 더 더해줌
      - 나머지 계산은 그대로
    *딕셔너리 정렬 까먹었음
    *올림하는 방식 (math.ceil)
    
    

*Referece


"""

# 1. 내 답
from collections import defaultdict
import math
def solution(fees, records):
    dict_ = defaultdict(list)
    for rec in records:
        t, n, s = rec.split(" ")
        dict_[n].append(t)
    
    for i in dict_:
        sum_t = 0     
        while dict_[i]:
            in_ = dict_[i].pop(0)
            h_in, m_in = in_.split(":")
            h_in, m_in = int(h_in), int(m_in)
            try:
                out_ = dict_[i].pop(0)
                h_out, m_out = out_.split(":")
                h_out, m_out = int(h_out), int(m_out)
            except:                
                h_out, m_out = 23,59
            sum_t += h_out*60 + m_out - (h_in*60 + m_in)
        if sum_t <= fees[0]:
            dict_[i]=fees[1]
        else:          
            dict_[i]=fees[1]+math.ceil((sum_t-fees[0])/fees[2])*fees[3]
        
    dict_sort = sorted(dict_.items(), key=lambda x : x[0])
    answer = [i[1] for i in dict_sort]
    return answer


# Reference
import math
def solution(fees, records):
    check = {}

    for record in records:
        time, number, status = record.split()
        time = time.split(':')
        time = int(time[0])*60 + int(time[1])
        if number not in check:
            check[number] = (0, time, status)
        if status == 'IN':
            check[number] = (check[number][0], time, status)
        elif status == 'OUT':
            total_time, in_time, _ = check[number]
            total_time += time - in_time
            check[number] = (total_time, time, status)

    result = {}

    for number in check.keys():
        total_time, time, status = check[number]
        if status == 'IN':
            total_time += 1439 - time
        fee = fees[1]
        if total_time <= fees[0]:
            result[number] = fee
        else:
            fee = fee + math.ceil((total_time - fees[0]) / fees[2]) * fees[-1]
            result[number] = fee

    return list(map(lambda x : x[1], sorted(result.items())))



