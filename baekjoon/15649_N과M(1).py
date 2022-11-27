"""
20221127

- No.: 15649
- type: 탐색, 백트래킹(Backtracking)
- Problem : N과 M(1)

*재귀함수 사용하기

## Reference
https://veggie-garden.tistory.com/24
https://velog.io/@nayeo0on/Backtracking
"""

# Reference
#N, M = map(int, input().split())
N,M=4,3
ans = []

def back():
    # 길이가 M이 됐을때 출력 (종료조건)
    if len(ans) == M: 
        print(" ".join(map(str, ans))) # 1 2 3 이런 상태로 출력하기 위해
        return 
    # 1부터 N까지 반복

    for i in range(1, N+1):
        if i not in ans: # 중복 확인
            ans.append(i) # 배열 추가
            back() # 재귀실행
            # 이걸 넘어왔다는 것은 종료조건에 걸렸다는 말이고
            # 다시 마지막 원소를 뺴줘야 함(ans가 global 변수이기 떄문)
            ans.pop()
            # 즉,
            # i=(1)
            # i=(2),3,4
            # i=(3),4 
            ###1,2,3에서 하나의 트리가 끝나고, 3을 다시 뺴줘야 1,2,4로 넘어감
            ###1,2,4 -> pop -> 1,2 -> pop -> 1 -> 1,3 -> 1,3,2 -> pop -> ...

            
back()
