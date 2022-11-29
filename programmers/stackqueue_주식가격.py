"""
20221129

- 프린터
- type: 스택/큐
- Level : 2
- Problem : 
    https://school.programmers.co.kr/learn/courses/30/lessons/42584
    
주의할점
    - 어렵게 만드려고 하지말고 일단 완전탐색으로 구현부터 할 것
    - 마지막에 어거지로 그냥 time 변수를 지정했는데, 좀더 깔끔한 refer를 참고
       - 미리 [0]* len(prices) 로 깔아놓고
       - 가격이 안떨어질때 +1 씩 시간을 추가함
       (나는 가격이 떨어질때 index끼리 빼서 구했음)
    - 두번째 loop에서 i가 아니라 i+1로 해줘야 같은 수 피할수 있음 (디테일 챙기자)
*Referece

"""

# 1. 내 답
def solution(prices):
    answer = []
    for i in range(len(prices)):
        time = 0
        for j in range(i+1,len(prices)):
            if prices[i]>prices[j]:
                time = j-i
                break
        if time==0:
            time = len(prices)-i-1
        answer.append(time)
    return answer
        
# Reference
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer