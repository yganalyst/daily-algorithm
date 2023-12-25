"""
20221217

- Dominator
- type: Leader
- level: Easy
- Problem : 
    https://app.codility.com/programmers/lessons/8-leader/dominator/

*주의할점
  - dictionary로 카운팅
  - 카운팅으로 정렬
  - 첫 숫자만 확인 하면 됨


*Referece
https://smecsm.tistory.com/226

"""

# 1. 내 답 (100%) - O(N*log(N)) or O(N)
from collections import Counter
def solution(A):
    if not A:
        return -1

    n=len(A)
    cnt_dict = Counter(A)
    cnt_dict = sorted(cnt_dict.items(), key=lambda x : -x[1])
    k,v = cnt_dict[0]
    if v>(n//2):
        return A.index(k)
    else:
        return -1

