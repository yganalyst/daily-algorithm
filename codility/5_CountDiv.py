"""
20221216

- CountDiv
- type: Prefix Sums
- level: Medium
- Problem : 
    https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/

*주의할점
  - 두번째로 성공
  - loop를 돌리는 순간 효율성 0점, 수학적으로 접근해야함
  - 결국 (0~B까지 K의 배수의 개수) - (0~A-1까지 K의 배수의 개수) 로 계산 가능
  *0도 divisible로 추가되어야함
  
  Reference 참고 
  - 비슷한 방식의 접근인데, 배수의 개수를 구할때 range로 굳이 안해도 되고
  - 배수의 개수는  "몫"을 통해 간단히 계산 가능
  - 시작점 (A)이 나누어 떨어질 경우가 (-) 연산으로 빠지니까 +1을 해주어야함
      * 이 경우로 0을 나누는 경우도 포함됨 (따로 생각할 필요 없음)
  
*Referece
https://sooho-kim.tistory.com/35

"""


# 1. 내 답 (100%) - O(1)
def solution(A, B, K):
    return len(range(0,B+1,K)) - len(range(0,A,K))

# 2. Reference (100%) - O(1)
def solution(A, B, K):
    QA = A//K
    RA = A%K
    QB = B//K
    count = QB-QA
    if RA ==0:
        count +=1
    return count

# 3. 내 답 (Performance 0%)
def solution(A, B, K):
    answer=0
    for i in range(A,B+1):
        if i%K==0:
            answer+=1
    return answer