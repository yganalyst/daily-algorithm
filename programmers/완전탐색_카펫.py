"""
20221131

- 카펫
- type: 완전탐색
- Level: 2
- Problem : 
    https://school.programmers.co.kr/learn/courses/30/lessons/42842
    
주의할점
  - 조금 헷갈렸으나 금방 풀었음
  - yellow 수로 사각형을 만드는 경우의 수를 먼저 생각 (약수를 뽑는 식으로)
  - 각 경우의 수에서 1줄로 감쌀때 brown수와 맞는지 체크
  - 맞으면 길이 맞춰서 반환하기
  ** 약수를 제곱근까지만 하니까 i가 무조건 작은쪽임

*Referece

"""

# 1. 내 답
import math
def solution(brown, yellow):

    for i in range(1,int(math.sqrt(yellow))+1):
        if yellow % i == 0:
            y_w = i
            y_h = yellow // i
            check = y_w*2 + y_h*2 + 4
            if check==brown:
                b_w=y_w+2
                b_h=y_h+2
                break

    answer = [max(b_w,b_h),min(b_w,b_h)]

    return answer

# 2. Reference (동일한 풀이임 조금 간단함)
def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]
        
    