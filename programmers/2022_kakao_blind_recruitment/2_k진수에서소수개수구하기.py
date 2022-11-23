"""
20221123

2022 KAKAO BLIND RECRUITMENT

2. k진수에서 소수 개수 구하기
- Problem : 
    https://school.programmers.co.kr/learn/courses/30/lessons/92335

주의할점
    10진수 -> n진수로 변환하는 함수 작성 (2~10진수만 가능)
    소수를 판별하는 코드 작성
        - 이코테 리뷰
        - 완전탐색(2~해당숫자)으로 모든 경우에 대해 나눠지는지를 보면 시간초과
        - 제곱근까지만 서칭하도록 개선
        - 여러개의 소수를 판별하는 에라토스테네스의 체도 리뷰해야함

*Referece
    https://joyjangs.tistory.com/35
    https://velog.io/@koyo/python-is-prime-number
    https://freedeveloper.tistory.com/391
"""

# 1. 내 답
import math
def getnum(n,k):
    result = ''
    while n:
        result = str(n%k) + result
        n//=k
    return result

def isprimenum(num):
    #for i in range(2,num):
    for i in range(2,int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    result = getnum(n,k)
    result = result.split("0")
    return sum([isprimenum(int(n)) for n in result if n and n!='1'])
