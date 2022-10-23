"""
20221023

- 최소직사각형
- type: 완전탐색
- Problem : 
    https://school.programmers.co.kr/learn/courses/30/lessons/86491
    
주의할점
  - 간단한 문제
    - 가로 세로 상관없이 긴게 가로로 보면 됨
    - 따라서 먼저 명함을 잘 정렬하고 (긴게 가로가 되게)
    - 그중에 max값으로 가로 세로 추출
  - Reference
    - 결국 이걸 max min으로 간단하게 할 수 있음
  - 내께 for문 1개라 성능은 낫지 않을까

*Referece

"""

# 1. 내 답
def solution(sizes):
    m_w = 0
    m_h = 0
    for ls_ in sizes:
        w,h = sorted(ls_)
        if m_w < w:
            m_w=w
        if m_h < h:
            m_h=h
    answer = m_w*m_h
    return answer

        
# 2. Reference : 간단하게
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
