"""
20220925

- 위장
- type: 스택/큐
- Problem : 
    https://school.programmers.co.kr/learn/courses/30/lessons/12906
    
주의할점
    스택 큐
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

# 2. 다른사람 풀이
def solution(arr):
   answer = []
   for i in arr:
       if answer[-1:] == [i]:
           continue
       answer.append(i)
   return answer
