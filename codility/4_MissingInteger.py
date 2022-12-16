"""
20221216

- MissingInteger
- type: Counting Elements
- level: Medium
- Problem : 
    https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/

*주의할점
  - 원샷 성공
  - 시간복잡도에서 루프 안에 있는 추가 연산을 주의하고, 가능하면 루프 밖으로 빼자

*Referece

"""
# 1. 내 답 (100%)
def solution(A):
    A = sorted(set(A))
    A = [i for i in A if i>0]
    if not A:
        return 1
    for i,v in enumerate(A, start=1):
        if i!=v:
            return i
    return i+1