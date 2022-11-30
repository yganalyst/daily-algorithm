"""
20221130

- 소수찾기
- type: 완전탐색
- level: 2
- Problem : 
    https://school.programmers.co.kr/learn/courses/30/lessons/42839
    
주의할점
  - 모든 경우의수 만 찾으면 되는데 거기서 해맴..
  1. DFS + 백트래킹을 이용한 방식
    - 1 2 3 일때 => 15가지(3*2*1 + 3*2 + *3)
    - 1
    - 12, 13
    - 123, 132
    - 2,
    - 21, 23
    - 213, 231
    - 3,
    - 31, 32
    - 312, 321
  2. Permutation을 이용한 방식
    - Permutation 라이브러리 이용하면 쉽다.
    - 리스트에서 r개를 나열하는 경우의 수(순서 O)
    - 가능한 r개 숫자마다 permutation 돌리면 끝
    - ex) numbers가 5면, r이 1~5인 각각의 경우에 대해 모든 permutation 계산
  3. Reference 참고 (놀라운 DFS 방식)
    - 1 2 3 일때
    - 1,
    - 12, 123
    - 13, 132
    - 2,
    - 21, 213
    - 23, 231
    - 3,
    - 31, 312
    - 32, 321

*Referece

"""

# 1. 내 답 (DFS + 백트래킹을 이용한 방식)
import math 
def isprimenum(num):
    if num <= 1:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if num % i==0:
            return False
    return True

def dfs_search(num, check_idx, numbers,result):
    for i in range(len(numbers)):
        if i in check_idx:
            continue
        new_num = num+numbers[i]
        check_idx.append(i)
        if isprimenum(int(new_num)):
            result.add(int(new_num))
        dfs_search(new_num, check_idx, numbers,result)
        check_idx.pop()

def solution(numbers):
    result=set()
    for i in range(len(numbers)):
        front_num = numbers[i]
        check_idx=[i]
        if isprimenum(int(front_num)):
            result.add(int(front_num))
        dfs_search(front_num, check_idx, numbers, result)

    print(result)
    answer = len(result)
    return answer

# 2. 내 답 (permutation 풀이)
from itertools import permutations
import math 

def isprimenum(num):
    if num <= 1:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if num % i==0:
            return False
    return True

def solution(numbers):
    result=set()
    for n in range(1,len(numbers)+1):
        comb_ = list(map(lambda x:"".join(x),permutations(numbers,n)))
        comb_ = set(comb_)
                     
        for num in comb_:
            if isprimenum(int(num)):
                result.add(int(num))
            
    answer = len(result)
    return answer


# 3. Reference (놀라운 DFS 방식)
primeSet = set()

def isPrime(number):
    if number in (0, 1):
        return False
    for i in range(2, number):
        if number % i == 0:
            return False

    return True

def makeCombinations(str1, str2):
    print(str1,str2)
    if str1 != "":
        if isPrime(int(str1)):
            primeSet.add(int(str1))

    for i in range(len(str2)):
        makeCombinations(str1 + str2[i], str2[:i] + str2[i + 1:])


def solution(numbers):
    makeCombinations("", numbers)

    answer = len(primeSet)

    return answer