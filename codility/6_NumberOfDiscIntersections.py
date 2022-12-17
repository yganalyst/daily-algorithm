"""
20221217

- NumberOfDiscIntersections
- type: Sorting
- level: medium
- Problem : 
    https://app.codility.com/programmers/lessons/6-sorting/number_of_disc_intersections/

*주의할점
   - 구현은 했으나 O(N**2)로 시간 효율성을 줄이지 못하였음..
   Reference
   1. 같은 O(N**2)이지만, 구현방법 참고
    - sorting 하지말고, (왼쪽 중심 원의 우측 끝 값) <= (오른쪽 중심 원의 좌측 끝 값)
    - 위 조건을 만족하면 1씩 count
    - 나도 for 문은 이렇게 구성했으므로, 어짜피 중복 카운트 안됨.
   2. O(N*log(N) or N) 방법
    - 아래 주석 참고, 어려움.. 

*Referece
https://sooho-kim.tistory.com/49
https://jayb-log.tistory.com/142?category=867478

"""
# 1. Reference
A = [1, 5, 2, 1, 4, 0]
def solution(A):
    arr = []
    for i, v in enumerate(A):
        arr.append((i-v, -1))          # 왼쪽 끝
        arr.append((i+v, 1))           # 오른쪽 끝

    arr.sort()                         # disc_edge를 정렬하여 왼쪽 끝 포인트부터 확인을 시작한다
    intersection = 0                   # 겹치는 원의 개수
    intervals = 0                      # 열리기 시작하여 아직 닫히지 않은 원의 개수

    for i,v in enumerate(arr):
        if v[1] == 1 :                 # 원의 오른쪽 끝
            intervals -= 1             # 열려있는 원이 하나 줄어든다.
        if v[1] == -1:                 # 원의 왼쪽 끝(새로 열릴 때)
            intersection += intervals  # 기존에 열려있던 원들과 겹치게 되어 총 쌍의 수에 포함이 된다.
            intervals += 1             # 열려있는 원이 하나 늘어난다.
            
    if intersection > 10000000:
        intersection = -1
    return intersection


# 2. Reference (Performance 0%) - O(N**2) - 구현이 간단해서 참고
def solution(A):
    count = 0
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if i+A[i]>=j-A[j]:
                count +=1
    if count > 10000000:
        count = -1
    return count



# 3. 내 답 (Performance 0%) - O(N**2)
def solution(A):
    N = len(A)
    result = set()
    sort_ls = sorted(enumerate(A), key=lambda x : -x[1])
    for i in range(N):
        n1_p, n1_r = sort_ls[i]
        n1_min = n1_p-n1_r
        n1_max = n1_p+n1_r
        for j in range(i+1,N):            
            n2_p, n2_r = sort_ls[j]
            n2_min = n2_p-n2_r
            n2_max = n2_p+n2_r
            if n1_min<=n2_min<=n1_max or n1_min<=n2_max<=n1_max:
                result.add((min(i,j), max(i,j)))
    answer = len(result)
    if answer > 10000000:
        return -1
    return answer

