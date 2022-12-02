"""
20221202

- 피로도
- type: 완전탐색
- Level: 2
- Problem : 
    https://school.programmers.co.kr/learn/courses/30/lessons/87946
    
주의할점
  - permutation을 활용하지 않고, 경우의수 짜는 연습해야함
  - DFS 풀이 시도했으나 실패 (k값을 계속 갱신시켜야함)
     -> 변수로 넣지말고 파라미터값으로 유지하면 가능함
  ** Reference DFS
     - 

*Referece

"""


# 1. 내 답 (permutation 활용)
from itertools import permutations
def solution(k, dungeons):
    comb_ = list(permutations(range(len(dungeons)), len(dungeons)))
    max_check=0
    for c in comb_:
        check=0
        init_k=k
        for i in c:
            a,b = dungeons[i]
            if init_k>=a:
                init_k-=b
                check+=1
        max_check = max(check, max_check)
    return max_check

# 2. Reference (DFS 활용)
answer = 0

def dfs_search(k, cnt, dungeons):
    global answer
    answer = max(cnt, answer)
    for i in range(n):
        if k>=dungeons[i][0] and not visited[i]:
            visited[i]=True
            dfs_search(k-dungeons[i][1], cnt+1, dungeons)
            visited[i]=False

def solution(k, dungeons):
    global n, visited
    n = len(dungeons)
    visited = [False]*n
    dfs_search(k, 0, dungeons)
    
    return answer


