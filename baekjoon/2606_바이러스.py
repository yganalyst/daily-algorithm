"""
20220721

- No.: 2606
- type: 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
- Problem : 하나의 부모노드에 연결된 모든 자식노드의 수 구하기

*graph 만들때 양방향으로 넣어야하는 실수 주의
*(1 2)이면 1에도 2추가, 2에도 1추가

"""

computers = int(input())
edges = int(input())
graph = [[] for _ in range(computers+1)]
for _ in range(edges):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for _ in graph:
    _.sort()

visited = [False]*computers
def dfs(node):
    print(node)
    visited[node-1]=True
    for next_node in graph[node]:
        if not visited[next_node-1]:
            dfs(next_node)
dfs(1)    
print(sum(visited)-1)

