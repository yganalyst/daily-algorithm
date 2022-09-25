"""
20220925

- 완주하지 못한 선수
- type: 해시
- Problem : 
    https://school.programmers.co.kr/learn/courses/30/lessons/42576

주의할점
- 간단하지만 계산복잡도에서 걸림
- 여러가지 풀이에 대한 이해

*Referece
https://datahub.tistory.com/8
https://coding-grandpa.tistory.com/85
https://www.daleseo.com/python-collections-counter/
"""

# 1. 리스트를 이용한 방법
def solution1(participant, completion):
    # 정렬
    participant.sort()
    completion.sort()
    # 작은리스트를 기준으로 하나씩 비교
    for i in range(len(completion)):
        # 다른게 나오면 리턴
        if participant[i]!=completion[i]:
            return participant[i]        
    # 마지막에 다른게 있는 경우
    return participant[-1]


# 2. 해시(딕셔너리 이용)
def solution2(participant, completion):
    answer = {}
    
    # 딕셔너리에 먼저 participant 추가 (중복인 경우 카운트)    
    # dict.get(key,val) : key에 해당하는 value 추출, 없으면 val반환
    for i in participant:
        answer[i] = answer.get(i, 0) + 1
       	    
    # completion에 따라 다시 -1   
    for j in completion:
        answer[j] -= 1
        
    # 1만 남은 value에 대하여 key값 반환   
    for k in answer:
        if answer[k] : return k

# 3. collection 모듈의 Counter 사용
#  - 2번 솔루션에서 key값별 count한 value를 자동으로 해줌
import collections
def solution3(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

# participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
# completion = ["josipa", "filipa", "marina", "nikola"]

