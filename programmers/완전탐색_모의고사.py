"""
20221023

- 모의고사
- type: 완전탐색
- Problem : 
    https://school.programmers.co.kr/learn/courses/30/lessons/42840
    
주의할점
  - 간단한 문제
  - Max 값 뽑을 때 enumerate를 활용해보자

*Referece

"""

# 1. 내 답
def solution(answers):
    cnt_1 = 0
    ans_1 = [1,2,3,4,5]
    cnt_2 = 0
    ans_2 = [2,1,2,3,2,4,2,5]
    cnt_3 = 0
    ans_3 = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        cnt_1 += answers[i] == ans_1[i%5]
        cnt_2 += answers[i] == ans_2[i%8]
        cnt_3 += answers[i] == ans_3[i%10]        
    
    ls_ = [(1,cnt_1),(2,cnt_2),(3,cnt_3)]
    max_cnt = max(cnt_1,cnt_2,cnt_3)
    answer = [k for k,v in ls_ if v == max_cnt]
    return answer

        
# 2. Reference : 간단하게
def solution(answers):
    ans_1 = [1,2,3,4,5]
    ans_2 = [2,1,2,3,2,4,2,5]
    ans_3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    for i in range(len(answers)):
        score[0] += answers[i] == ans_1[i%5]
        score[1] += answers[i] == ans_2[i%8]
        score[2] += answers[i] == ans_3[i%10]        
    
    answer=[]
    for idx,v in enumerate(score, start=1):
        if v==max(score):
            answer.append(idx)
    return answer

