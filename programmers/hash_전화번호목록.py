"""
20220929

- 완주하지 못한 선수
- type: 해시
- Problem : 
    https://school.programmers.co.kr/learn/courses/30/lessons/42577

주의할점
- 간단하지만 계산복잡도에서 걸림
- 여러가지 풀이에 대한 이해

*Referece
https://whwl.tistory.com/200
https://iambeginnerdeveloper.tistory.com/157


"""

# 1. 완전 탐색 방식 -> 효율성에서 통과 X
def solution(participant, completion):
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


# 2. 집합 자료구조 이용 -> ["77","55","125","126"] 이런 케이스가 고려되지 않음
def solution(phone_book):
    n_ls = sorted(set([len(i) for i in phone_book]))
    for n in n_ls:
        unique_num = set([i[:n] for i in phone_book])
        print(unique_num)
        if len(unique_num) < len(phone_book):
            return False
        phone_book = [i for i in phone_book if i not in unique_num]
    return True

    
# 3. (참고) 문자열 정렬을 기반으로 앞뒤 비교 -> 통과
def solution(phone_book):
    phone_book = sorted(phone_book)
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
        else:
            continue
    return True

