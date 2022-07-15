"""
 - BFS (Breadth Frist Search)
 - type : DFS/BFS


"""
from collections import deque

def bfs(graph, start, visited):
    queue = deque([1])
    visited[start]=True
    
    while queue:
        v=queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
            
# 각 노드(index)가 연결된 다른 노드 정보를 리스트로 표현
graph = [
         [],
         [2,3,8], # 1번 노드는 2,3,8에 연결되어 있음
         [1,7],
         [1,4,5],
         [3,5],
         [3,4],
         [7],
         [2,6,8],
         [1,7]
         ]
visited = [False]*9

bfs(graph, 1, visited)
