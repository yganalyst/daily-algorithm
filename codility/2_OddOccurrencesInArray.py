"""
20221213

- 
- type: Arrays
- level: Easy
- Problem : 
        https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/
        
*주의할점
  - 결국 array의 원소별로 카운트해서 홀수개인 원소를 찾는 문제
  1. 내답
    - Counter로 원소별 개수를 미리 카운트하고, 홀수개인 원소를 print (복잡도가 괜찮진 않을듯)
  2. Reference
    - 정렬 -> 0, 2, 4 , ... 이런식으로 인덱스를 바로 다음 인덱스와 비교
    - 같지 않으면 그 숫자 반환 (다른건 짝수니까 그 i가 답이 됨)
 

*Referece
https://algoisanswer.tistory.com/31
"""

# 1. 내 답 (100점)
from collections import Counter
def solution(A):
    dict_ = Counter(A)
    for k,v in dict_.items():
        if v%2!=0:
            answer = k
            break
    return answer

# 2. Reference
def solution(A):
    # write your code in Python 3.6
    A.sort()
    if len(A) == 1:           # 원소가 하나 뿐일때
        return A[0]
    for i in range(0, len(A), 2):
        if i == len(A)-1:     # 마지막 원소가 답일때
            return A[i]
        if A[i] == A[i+1]:    # 다음숫자랑 같은지 판단
            continue
        else:
            return A[i]
