"""
 - DFS (Depth-Frist Search)
 - type : DFS/BFS

*1->2->7->6->8 (다시 재귀호출에서 7의 loop로 돌아옴)->3->4->5

"""

def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v,end=' ')
    
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
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
dfs(graph, 1, visited)
