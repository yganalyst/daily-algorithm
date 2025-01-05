"""
20221215

- PermCheck
- type: Counting Elements
- level: Easy
- Problem : 
    https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/

*주의할점
  - 

*Referece


"""

# 1. 내 답
def solution(A):
    A = sorted(A)
    for i,v in enumerate(A):
        if v!=i+1:
            return 0
    return 1

# 2. 내 답(20250105)
def solution(A):
    n=len(A)
    un = len(set(A))
    if n!=un:
        return 0
    A.sort()
    if A[-1]==n:
        return 1
    return 0

