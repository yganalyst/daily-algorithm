"""
20220721

- No.: 2178
- type: 그래프 이론, 그래프 탐색, 너비 우선 탐색
- Problem : (1,1)에서 (N,M)로 가는 최단경로길이 계산

*최단경로 길이를 찾기 위해서는 graph에 방문할때마다 직전 노드 +1를 graph에 취해주기!!!


"""
from collections import deque

N,M = map(int,input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,input())))


s_n,s_m=1,1
nx=[-1,1,0,0]
ny=[0,0,-1,1]
queue=deque([])
queue.append((s_n,s_m))
while queue:
    node_n, node_m = queue.popleft()
    for i in range(4):
        new_node_n = node_n + nx[i]
        new_node_m = node_m + ny[i]
        if (new_node_n < 1) | (new_node_n > N) | (new_node_m < 1) | (new_node_m > M):
            continue
        if graph[new_node_n-1][new_node_m-1]==0:
            continue
        if graph[new_node_n-1][new_node_m-1]==1:
            graph[new_node_n-1][new_node_m-1]=graph[node_n-1][node_m-1]+1
            queue.append((new_node_n, new_node_m))

print(graph[N-1][M-1])
