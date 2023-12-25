"""
 - 소수의 판별

*소수: 2보다 큰 자연수 중에서 1과 자기 자신을 제외한 자연수로는 나누어떨어지지 않는 자연수

*1. 모든 수 탐색방법은 수가 커질수록 비효율적
*2. 제곱근 수 까지만 확인하는 방법으로 개선
  - 16의 약수 : 1, 2, 4, 8, 16 일때 2와 8은 결국 대칭
  - 따라서 제곱근인 4까지만 확인하면 된다는 소리
*3. N보다 작거나 같은 모든 소수를 찾을때 사용 - 에라토스테네스의 체
  1) 2부터 N까지의 모든 자연수를 나열
  2) 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾음
  3) 남은 수 중에서 i의 배수를 모두 제거(i는 제거 X)
  4) 2)~3)과정 반복
"""

# 1. 모든 수 탐색방법 : O(X)
def is_prime_number(x):
    for i in range(2,x):
        if x % i ==0:
            return False
    return True
print(is_prime_number(4))

# 2. 제곱근까지만 탐색 : O(X^(1/2))
import math
def is_prime_number(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x % i ==0:
            return False
    return True
print(is_prime_number(4))

# 3. 에라토스테네스의 체
import math
n=1000
array=[True for i in range(n+1)]  # 소수판별 table 초기화 0부터 시작
for i in range(2, int(math.sqrt(n))+1):  # 2~n의 제곱근까지 확인
    if array[i]==True:   # i가 소수인 경우(남은 수인 경우)
        # 이하는 배수를 지우는 작업
        j=2     
        while i*j <= n:
            array[i*j]=False
            j+=1
for i in range(2, n+1):
    if array[i]:
        print(i, end=' ')










