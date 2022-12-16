"""
20221217

- Triangle
- type: Sorting
- level: Easy
- Problem : 
    https://app.codility.com/programmers/lessons/6-sorting/triangle/

*주의할점
  - P < Q < R 조건은 어차피 필요 없음 (원소 3개를 뽑는 문제임)
  - 1,2,3,6,8,9 로 정렬되어 있다고 했을때, 
    - 1,2,3에서 (2+3)>1과 (3+1)>2은 오름차순 정렬로 인해 판단할 필요 없음
    - 따라서 (1+2)>3 을 만족하는지만 판단하면 됨
  - 이렇게 1,2,3 -> 2,3,4 -> 3,4,5 순으로 한번의 loop만 돌면 종료

*Referece
https://sooho-kim.tistory.com/48
"""

# 1. Reference 
def solution(A):
    if len(A)<3:
        return 0
    A = sorted(A)
    for i in range(len(A)-2):
        if A[i]+A[i+1] > A[i+2]:
            return 1
    return 0

