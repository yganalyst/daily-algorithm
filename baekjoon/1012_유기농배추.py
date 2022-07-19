"""
20220719

- No.: 1012
- type: 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
- Problem : graph 탐색하면서 인접해있는 경우가 몇가지인지 카운트 하기

*book의 음료수 얼려먹기랑 동일한 유형
*graph에 바로 방문처리를 해야 간편.. 어렵다
*시작노드 -> 재귀타면 최종 True 못타면 최종 False (이게 핵심, print가 아닐땐 최종값만 인식함)
*재귀타면 방문처리를 graph에 해주는게 두번째 핵심
*기본 재귀 깊이 제한(recursionlimit)은 1000이기 떄문에, 확장시켜주는 것 필수!!!
"""

import sys
sys.setrecursionlimit(10000)

def dfs(s_n,s_m):
    if (s_m < 0) | (s_m >= M) | (s_n < 0) | (s_n >= N):
        return False
    if graph[s_n][s_m]==1:
        graph[s_n][s_m]=0
        dfs(s_n-1,s_m)
        dfs(s_n+1,s_m) # 2
        dfs(s_n,s_m-1)
        dfs(s_n,s_m+1) # 1
        return True
    return False

test_case = int(input())
for _ in range(test_case):
    M,N,cnt = map(int,input().split())
    graph = [[0]*M for i in range(N)]
    for i in range(cnt):
        m,n = map(int,input().split())
        graph[n][m] = 1    
    
    result=0
    for i in range(N):
        for j in range(M):
            if dfs(i,j):
                result+=1
    print(result)
