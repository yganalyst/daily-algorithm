"""
20221215

- FrogRiverOne
- type: Counting Elements
- level: Easy
- Problem : 
    https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/

*주의할점
  - 시간 복잡도 주의
  - 앞선 문제처럼 매 loop마다 연산이 들어갈때 (sum, in 연산자 등) N**2이 되버림
  - 따라서 set 자료구조를 이용해서 add해주는 방법으로 변경
  Reference
  - Refer도 같은 방식인데, set 대신 [0]*X개의 원소를 먼저 만들고 삽입하는 방식으로 진행
  - zero값인 경우(아직 안채워짐)에만 1로 채우고, 채워진 숫자가 X와 같아지면 그 index 반환

*Referece
https://wayhome25.github.io/algorithm/2017/05/30/FrogRiverOne/

"""

# 1. 내 답 (수정) O(N)
def solution(X, A):
    check=set()
    for i,v in enumerate(A):
        if v>=1 and v<=X:
            check.add(v)
        if len(check)==X:
            return i
    return -1

# 2. 내 답 (퍼포먼스 탈락) O(N ** 2)
def solution(X, A):
    ls = list(range(1,X+1))
    for i,v in enumerate(A):
        if v in ls:
            ls.remove(v)
        if not ls:
            return i
    return -1

# 3. Reference
def solution(X, A):
    check = [0] * X
    check_sum = 0
    for i in range(len(A)):
        if check[A[i]-1] == 0:
            check[A[i]-1] = 1
            check_sum += 1
            if check_sum == X:
                return i
    return -1



