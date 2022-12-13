"""
20221213

- FrogJmp
- type: Time Complexity
- level: Easy
- Problem : 
    https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/
        
*주의할점
  - 다른사람들도 대부분 내 방식으로 풀었음
*Referece

"""

# 1. 내 답 (100점)
def solution(X, Y, D):
    gap = Y-X
    if gap % D == 0:
        return gap // D
    else:
        return gap // D + 1
