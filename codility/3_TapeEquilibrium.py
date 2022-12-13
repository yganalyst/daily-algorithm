"""
20221214

- TapeEquilibrium
- type: Time Complexity
- level: Easy
- Problem : 
    https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/

*주의할점
  - 시간 복잡도 주의
  - N개 요소를 가진 list를 sum하는 것도 O(N) 임
  - 전체 loop는 어쩔 수 없고, sum하는 값을 원소 하나씩 슬라이싱해야함!

*Referece
https://haerang94.tistory.com/70
https://sooho-kim.tistory.com/14

"""

# 1. 내 답 (수정)
def solution(A):
    part1=A[0]
    part2=sum(A[1:])
    answer=abs(part1-part2)
    for i in range(1,len(A)-1):
        part1+=A[i]
        part2-=A[i]
        answer = min(answer, abs(part1-part2))
    return answer


# 2. 내 답 (퍼포먼스 탈락) O(N*N)
def solution(A):
    answer = 100000*1000
    for i in range(1,len(A)):
        result = abs(sum(A[:i]) - sum(A[i:]))
        answer = min(answer, result)
    return answer





