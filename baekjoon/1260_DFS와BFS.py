"""
20220718

- No.: 1260
- type: 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
- Problem : Edge 리스트에 대하여 DFS와 BFS 결과 출력

*function을 복잡하게 만들지말고, graph를 간단하게 바꾸자
*node마다 neighbor node list를 가진 이중 리스트로

reference
https://www.devchopin.com/blog/96/

"""

from collections import deque

N,M,start_node = map(int,input().split())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(len(graph)):
    graph[i].sort()

def dfs(start_node):
    print(start_node,end=' ')
    visited1[start_node-1] = True    
    for next_node in graph[start_node]:
        if not visited1[next_node-1]:
            dfs(next_node)

def bfs(start_node):
    queue = deque()
    queue.append(start_node)
    visited2[start_node-1] = True
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for next_node in graph[node]:
            if not visited2[next_node-1]:
                visited2[next_node-1] = True
                queue.append(next_node)    

visited1 = [False]*N
dfs(start_node)
print()
visited2 = [False]*N
bfs(start_node)  

# ## 기존 코드 실패.. 
# N,M,start_node = map(int,input().split())
# edge_list=[]
# for i in range(M):
#     edge_list.append(list(map(int,input().split())))

# def dfs(start_node):
#     print(start_node,end=' ')
#     visited1[start_node-1] = True
#     neighbor_ls = sorted([i for i in edge_list if start_node in i])[:]
#     for ex_ in neighbor_ls:
#         ex_cop = ex_[:]
#         ex_cop.remove(start_node)
#         next_node = ex_cop[0]
#         if not visited1[next_node-1]:
#             dfs(next_node)

# def bfs(start_node):
#     queue = deque()
#     queue.append(start_node)
#     visited2[start_node-1] = True
#     while queue:
#         node = queue.popleft()
#         print(node, end=' ')
#         neighbor_ls = sorted([i for i in edge_list if node in i])[:]
#         for ex_ in neighbor_ls:
#             ex_cop = ex_[:]
#             ex_cop.remove(node)
#             next_node = ex_cop[0]
#             if not visited2[next_node-1]:
#                 visited2[next_node-1] = True
#                 queue.append(next_node)

# visited1 = [False]*N
# dfs(start_node)
# print()
# visited2 = [False]*N
# bfs(start_node)  