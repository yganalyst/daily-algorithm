"""
20221122

2022 KAKAO BLIND RECRUITMENT

3. 주차요금계산
- Problem : 
    https://school.programmers.co.kr/learn/courses/30/lessons/92341  

주의할점
    딕셔너리 정렬
    올림하는 방식 (math.ceil로만?)
    

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
        print(sum_t)
        if sum_t <= fees[0]:
            dict_[i]=fees[1]
        else:          
            dict_[i]=fees[1]+math.ceil((sum_t-fees[0])/fees[2])*fees[3]
        
    dict_sort = sorted(dict_.items(), key=lambda x : x[0])
    print(int(3.6))
    answer = [i[1] for i in dict_sort]
    return answer


