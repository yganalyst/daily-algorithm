"""
20220925

- 위장
- type: 스택/큐
- Problem : 
    https://school.programmers.co.kr/learn/courses/30/lessons/12906
    
주의할점
  - 스택,큐와 같은 자료구조 원리를 이용하는 아이디어를 활용
    - 결과 list의 마지막 값과 비교해서 다를때 추가해주면 됨

*Referece

"""

arr = [1,1,3,3,0,1,1]

# 1. 내 답
def solution(arr):
    answer = [arr[0]]
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer

# 2. Reference
def solution(arr):
   answer = []
   for i in arr:
       if answer[-1:] == [i]:
           continue
       answer.append(i)
   return answer
