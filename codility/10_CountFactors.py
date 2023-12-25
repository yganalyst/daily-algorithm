"""
20221217

- CountFactors
- type: Prime and composite numbers
- level: Easy
- Problem : 
    https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/count_factors/

*주의할점
  - Idea는 같은데, 제곱수 판별 떄문에 효율성 저하
  - list에 in 연산자로 추가 연산이 필요하게돼서 효율성 1개 case가 실패..
  - 결국 제곱수까지만 확인하되,
    - 약수이면 +2
    - 제곱수면 +1하고 종료
  
*생각한 Test case
 - 1
 - 2
 - 3
 - 9
 - 16
 - 2147483647

*Referece
https://sohyunwriter.tistory.com/100

"""

# 1. Reference
import math
def solution(N):
    n_sqrt = math.sqrt(N)
    answer=0
    for i in range(1,int(n_sqrt)+1):
        if N%i==0:
            if i*i==N:
                answer+=1
                break
            else:
                answer+=2
    return answer

# 2. 내 답 - O(sqrt(N)) - 92%
import math
def solution(N):

    n_sqrt = math.sqrt(N)
    save_ls = []
    for i in range(1,int(n_sqrt)+1):
        if i in save_ls:
            break
        if N%i==0:
            save_ls.append(i)
            save_ls.append(N//i)

    return len(set(save_ls))



