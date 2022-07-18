"""
20220718

- No.: 1260
- type: 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
- Problem : Edge 리스트에 대하여 DFS와 BFS 결과 출력

*재귀함수 사용하기

"""

N,M,s_node = 4,5,1
edge_list = [[1,3],
             [1,2],
             [1,4],
             [2,4],
             [3,4]]
edge_list = sorted(edge_list)

# DFS
# 1 -> 2 -> 4 -> 3



visited = [False]*N
s_node=1
visited[s_node-1] = True
next_nodes = [i for i in edge_list if s_node in i][:]
for ex_ in next_nodes:
    ex_ = next_nodes[0][:]
    ex_.remove(s_node)
    ex_
    next_node = [set(ex_) - set([s_node])][0][0]
    
    
    if (i[0]==1):
        
