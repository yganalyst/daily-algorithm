"""
20221213

- CyclicRotation
- type: Arrays
- level: Easy
- Problem : 
        https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/
    
주의할점
  - N,K의 범위 주의 (N=0 인 경우 나머지 계산이 안되므로 고려해줘야함)

*Referece

"""


# 1. 내 답 (100점)
def solution(A, K):
    n=len(A)
    if n==0:
        return A
    key = K%n
    if key==0:
        return A
    return A[-key:]+A[:n-key]
