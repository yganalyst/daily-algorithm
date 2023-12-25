"""
20221213

- PermMissingElem
- type: Time Complexity
- level: Easy
- Problem : 
    https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/
        
*주의할점
  - 문제를 잘 이해하고 예외처리 신경써야함
  1. 수정
  - len(A)==0 일때, [1]이어야 하므로 1을 return해야함
  - [1,2,3,4] 일때, [1,...,(N+1)]이므로 5를 return해야함
  2. 수정
  - [1,...,(N+1)]까지 리스트를 먼저 만들어 놓고, 주어진 리스트를 빼면 남은 수가 됨

*Referece

https://velog.io/@zioo/Codility-Lesson-3-2.-PermMissingElem-python

"""

# 1. 내 답 (수정) - 경우의 수 반영한 케이스
def solution(A):
    A.sort()
    if len(A) == 0:
        return 1
    for i in range(len(A)):
        if A[i] != i+1:
            return i+1
    return len(A)+1

# 2. 내 답 (수정) - (합으로 계산)
def solution(A):
    return sum(list(range(1,len(A)+2)))-sum(A)
