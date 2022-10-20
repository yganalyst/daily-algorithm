"""
20221020

- 프린터
- type: 스택/큐
- Problem : 
    https://school.programmers.co.kr/learn/courses/30/lessons/42587
    
주의할점
  - 효율성에 걸릴까 걱정하긴 했으나, 측정을 안했음
  - ID를 매겨줄 수 밖에 없으며, 문제대로 구현만 하면 되는 문제임

*Referece

"""

# 1. 내 답
def solution(priorities, location):
    id_pr = list(zip(range(len(priorities)),priorities))
    n=0
    while id_pr:
        cur_ = id_pr.pop(0)
        if any([_pr for _id, _pr in id_pr if _pr > cur_[1]]):
            id_pr.append(cur_)
            continue
        else:
            n+=1

        if cur_[0]==location:
            return n
        
    