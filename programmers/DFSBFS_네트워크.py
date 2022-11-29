"""
20221129

- 네트워크
- type: DFS/BFS
- Problem : 
    https://school.programmers.co.kr/learn/courses/30/lessons/43162
    
주의할점
  - 기존에 이코테에서 풀었던 얼음틀 문제처럼 접근했는데, 큰 실수..
  - DFS로 탐색할때, 인접 노드로 찾는게 아니라 연결되어 있는 노드로 찾아야함 
  - 두가지 DFS
    - 1. computers matrix를 먼저 edge list graph 형태로 전환하여 편하게 풀기
    - 2. computer matrix 자체로 풀기

*Referece

"""

# 1. 내 답 첫번재
def dfs_search(cur_node,graph,visited):
    visited[cur_node]=True
    for next_node in graph[cur_node]:
        if not visited[next_node]:
            dfs_search(next_node,graph,visited)
    return 1

def solution(n, computers):
    answer = 0
    visited = [False]*n
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            if computers[i][j]==1:
                graph[i].append(j)

    for node in range(n):
        if not visited[node]:
            answer+=dfs_search(node,graph,visited)

    return answer

# 2. 내 답 두번째
def dfs_search(n,node, computers,visited):
    visited[node]=True
    for next_node in range(n):
        if next_node == node or computers[node][next_node]==0:
            continue
        if not visited[next_node]:
            dfs_search(n,next_node, computers,visited)
    return 1

def solution(n, computers):
    answer = 0
    visited = [False]*n
    for start_node in range(n):
        if not visited[start_node]:
            answer+=dfs_search(n,start_node, computers,visited)
    return answer