"""
20221216

- MaxCounters
- type: Counting Elements
- level: Medium
- Problem : 
    https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/

*주의할점
  - 세번째 답은 전체 loop (M), max 계산(N)으로 O(N*M) 복잡도가 나왔음
  - 두번째 답은 max를 그때마다 갱신해 주는 방식으로 성능이 조금 증가했지만 그래도 100은 안됨
  - 여기서 매번 새로운 리스트를 만드는 ([max_num]*N) 에서 시간이 오래걸림
  - 첫번째 답 (Reference 참고)
    - 연산(비교, 게산 등) 대신 대입하는 방법으로 대체하자
    - max_counter를 유지하는 check_num을 저장해두고
    - max_num은 계속해서 갱신해주다가, N+1을 만날때만 check_num 갱신
    - check_num에다가 누적해주는 식으로 계속 계산해주고
    - 마지막까지 0인 경우가 있으므로 (한번도 안나온 원소) 이 값들은 마지막에, check_num으로 대체

*Referece
https://imksh.com/68

"""
# 1. Reference 참고 (100%)
def solution(N, A):
    opers = [0]*N
    check_num = 0
    max_num=0
    for i in A:
        if i<=N:
            if opers[i-1] < check_num:
                opers[i-1] = check_num
            opers[i-1] += 1
            max_num = max(max_num, opers[i-1])
        else:
            check_num=max_num
    for i in range(N):
        if opers[i] < check_num:
            opers[i] = check_num
    return opers

# 2. 내 답 (Performance 60%)
def solution(N, A):
    opers=[0]*N
    max_num=0
    for i in A:
        if i==N+1:
            opers = [max_num]*N
        else:
            opers[i-1]+=1
            max_num = max(max_num, opers[i-1])
    return opers

# 3. 내 답 (Performance 50%) - O(N*M)
def solution(N, A):
    opers=[0]*N
    for i in A:
        if i==N+1:
            opers = [max(opers)]*N
        else:
            opers[i-1]+=1
    return opers

