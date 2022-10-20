"""
20220925

- 올바른 괄호
- type: 스택/큐
- Problem : 
    https://school.programmers.co.kr/learn/courses/30/lessons/12909
    
주의할점
 - ())) ((()
 - ( (   )  )  (  ) )      

*Referece


"""

from collections import deque
def solution(s):
    if s[0]==")" or s[-1]=="(":
        return False

    q = deque(s)
    check_n = 0
    while q:
        cur = q.popleft()
        if cur == "(":
            check_n+=1
        else:
            check_n-=1
        if check_n<0:
            return False
    return True


