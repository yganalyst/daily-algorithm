"""
20221218

- AbsDistinct
- type: Caterpillar method
- level: Easy
- Problem : 
    https://app.codility.com/programmers/lessons/15-caterpillar_method/abs_distinct/

*주의할점
  - 이렇게 풀라는 의도는 아닌거같은데.. 쩃든 100%
  
*생각한 Test case
  - 

*Referece

"""

# 1. 내 답
def solution(A):
    return len(set(map(abs, A)))