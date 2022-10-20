"""
20221019

- 위장
- type: 해시
- Problem : 
    https://school.programmers.co.kr/learn/courses/30/lessons/42578    
    
주의할점
  - 경우의 수 주의
    - (의상1 + 1)*(의상2 + 1) *(의상3 + 1) - 1
    - 아무것도 안입은 경우(+1)를 포함해서 모두 곱해주고 아무것도 안입는 경우(-1)를 고려하면 됨
  - Dictionary 만드는 방식 주의  
    - dict는 key값으로 iteration을 식별함 (in 으로 확인해서 저장)
    - Counter(["a1","a1","a2","a2","a2"]) -> {"a1":2,"a2":3}

*Referece
https://coding-grandpa.tistory.com/m/88
https://jjuha-dev.tistory.com/m/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%9C%84%EC%9E%A5LV2-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython

"""

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

# 1. 일반 Dictionary 방식
def solution(clothes):
    _dict = {}
    for v,k in clothes:
        if k in _dict:
            _dict[k]+=1
        else:
            _dict[k]=1    
    answer = 1
    for n in _dict.values():
        answer*=(n+1)
    return answer-1


# 2. Counter를 이용하여 Dict 간편하게 만들기
from collections import Counter
def solution(clothes):
    _dict = Counter([k for v,k in clothes])
    answer = 1
    for n in _dict.values():
        answer*=(n+1)
    return answer-1