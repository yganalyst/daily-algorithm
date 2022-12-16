"""
20221216

- PassingCars
- type: Prefix Sums
- level: Easy
- Problem : 
    https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/

*주의할점
  - 원샷 성공
  - 로직
    - [0,1,0,1,1] loop는 해당 list기준 
    - 0이 나올때마다 해당 시점에서 동쪽으로 가는 차량을 누적해서 계산
    - 이때 1을 만나면 현재 시점에서 누적한 값만큼 더해줌
    - 이런식으로 누적 sum을 이용하면 loop 한번만에 끝내기 가능
    (index0 차량 먼저 계산 -> index3 차량 계산 이런식으로하면 중복 시간복잡도가 발생)

*Referece

"""

# 1. 내 답 (100%) - O(N)
def solution(A):
    answer = 0
    check_east = 0
    for i in A:
        if i==0:
            check_east+=1
        else:
            answer += check_east
    if answer > 1000000000:
        return -1
    return answer