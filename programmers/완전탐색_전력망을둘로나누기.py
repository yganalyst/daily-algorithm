"""
20221202

- 전력망을 둘로 나누기
- type: 완전탐색
- Level: 2
- Problem : 
    https://school.programmers.co.kr/learn/courses/30/lessons/86971
    
주의할점
   1. DFS 방법으로 풀이   
   - 하나의 edge가 없는 모든 경우에 대해 graph와 visited를 초기화
   - graph가 크지 않으면 adjacent matrix로 만들자
   - 하나의 트리에 몇개 노드가 있는지 count하기 위해 global 변수의 지정이 필요했음
   
   2. BFS 로도 풀어보자
   - 큰 차이는 없음
   - 재귀탐색을 안하기 때문에 cnt를 global하게 정의할 필요 없음 (return해주면 됨)
   - init_graph함수를 없애고, wires[:i] + wires[i+1:] 이런식으로 한개 인덱스 제외하기
   - 코드는 짧아지나 계산복잡도는 차이 없음
** Reference

"""


# 1. 내 답 (DFS search 활용)
def dfs(node,graph,visited):
    global cnt
    cnt+=1
    visited[node]=True
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node, graph, visited)
    
def init_graph(remove_idx,n,wires):
    visited = [False]*(n+1)
    graph = [[] for _ in range(n+1)]
    for i,pair in enumerate(wires):
        if i==remove_idx:
            continue
        a,b=pair
        graph[a].append(b)
        graph[b].append(a)
    return visited, graph

def solution(n, wires):
    global cnt
    min_diff = 100
    for i in range(len(wires)):
        visited, graph = init_graph(i,n,wires)
        result = []
        for start_node in range(1,n+1):
            if not visited[start_node]:
                cnt=0
                dfs(start_node,graph,visited)   
                result.append(cnt)
        min_diff = min(min_diff, abs(result[0]-result[1]))
    return min_diff


# 2. 내 답 (BFS 활용)
from collections import deque
def bfs(node,graph,visited):
    cnt=0
    q = deque()
    q.append(node)
    visited[node]=True
    while q:
        cur_node = q.popleft()
        for next_node in graph[cur_node]:
            if not visited[next_node]:
                visited[next_node]=True
                q.append(next_node)
                cnt+=1
    return cnt        

def solution(n, wires):
    min_diff = 100
    for i in range(len(wires)):
        visited = [False]*(n+1)
        graph = [[] for _ in range(n+1)]
        wires_ls = wires[:i] + wires[i+1:]
        for a,b in wires_ls:
            graph[a].append(b)
            graph[b].append(a)        
        
        result=[]
        for start_node in range(1,n+1):
            if not visited[start_node]:
                cnt=bfs(start_node,graph,visited)   
                result.append(cnt)
        min_diff = min(min_diff, abs(result[0]-result[1]))
    return min_diff





