"""
20221021

- H-Index
- type: 정렬
- Problem : 
    https://school.programmers.co.kr/learn/courses/30/lessons/42747
    
주의할점
  - 간단해보이지만 어려웠다..
  - 첫 실수는 [6,5,5,5,3,2]와 같이 H-index 후보 값이 리스트에 없는 Case
    - 이때 후보값을 리스트에서 찾지말고, 카운트한(len)값을 출력해야함
    - 이생각까지 도달했으나 실패.
  - Reference 들을 참고하자
    - 결국 "인덱스 값 = 논문의 수"라는 점을 활용해보려고 해야함

*Referece
https://latte-is-horse.tistory.com/195
https://ssuamje.tistory.com/47

"""

# 1. Reference
def solution(citations):
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if i+1 > citations[i]:
            return i
    return len(citations)
        
# 2. Reference : 신박하지만 이해가 잘 안됨(URL 참고)
def solution(citations):
    n_ls = sorted(citations, reverse=True)
    answer = max(map(min, enumerate(n_ls, start=1)))
    return answer

