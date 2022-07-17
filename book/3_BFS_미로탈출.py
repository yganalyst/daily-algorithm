"""
 - 미로 탈출
 - type : BFS

*어려워
*탐색하고 방문처리가 아닌, 최단거리를 입력주면 간단하다!
*첫번째 시작위치를 다시 방문할 수 있어서 3으로 되지만, 결과에는 지장 X
"""
from collections import deque

N,M = map(int,input().split())
graph=[]
for i in range(N):
    graph.append(list(map(int,input())))

def routing(head,x,y):
    point_new = [x,y][:]
    if head==0:
        point_new[0]-=1
    elif head==1:
        point_new[1]+=1
    elif head==2:
        point_new[0]+=1
    elif head==3:
        point_new[1]-=1
    return point_new[0],point_new[1]

def maze_bfs(x,y):        
    queue = deque([])
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        for head in range(4):
            nx,ny = routing(head,x,y)
            if (nx < 0) | (nx >= N) | (ny < 0) | (ny >= M):
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
    return graph
        
maze_bfs(1,1)

