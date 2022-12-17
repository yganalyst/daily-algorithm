"""
20221217

- EquiLeader
- type: Leader
- level: Easy
- Problem : 
    https://app.codility.com/programmers/lessons/8-leader/equi_leader/

*주의할점
  - 전체에 대해 먼저 counting
  - 문자 하나씩 돌면서 left를 만들고 (누적으로), 그만큼 전체에서 빼줌 (right)
  - left의 leader 추출
    *매번 left의 루프는 다시 갱신하지말고, 이전 max값 확인하는 방식으로 업데이트
    *어짜피 제일 큰 cnt를 가지는 원소가 left가 됨
  - left의 leader에 해당하는 right의 cnt도 leader가 되는지 확인  

*Referece
https://smecsm.tistory.com/227

"""

# 1. Reference - O(N)
from collections import Counter
def solution(A):
    result = 0
    total_n = len(A)
    total_cnt = Counter(A)

    sub_n =0
    sub_cnt = {}
    sub_leader_cnt = 0
    sub_leader = ''
    for i in A:
        total_cnt[i]-=1
        total_n-=1

        if i in sub_cnt:
            sub_cnt[i]+=1
        else:
            sub_cnt[i]=1
        sub_n+=1
        
        if sub_cnt[i] > sub_leader_cnt:
            sub_leader=i
            sub_leader_cnt=sub_cnt[i]
        
        if sub_leader_cnt > sub_n/2 and total_cnt[sub_leader] > total_n/2:
            result += 1
    return result

        

