"""
20221201

- 게임 맵 최단거리
- type: DFS/BFS
- Problem : 
    https://school.programmers.co.kr/learn/courses/30/lessons/1844
    
주의할점
  - DFS로 하니까 먼저 찾은 경로가 최단경로가 아니여도 종료될 수 있음
    - 이걸 방지하려면 방문처리를 계속 갱신해주어야함 (너무 복잡해짐)
  - BFS로 풀면 간단해짐
  **핵심은 graph에 방문처리할때 이전에 왔던 칸의 값을 더해주는 것 (누적)
  **이코테 미로찾기(동일한 문제)

*Referece

"""

# 1. 내 답 BFS(성공)
from collections import deque
def is_valid(point,maps):
    n=len(maps)
    m=len(maps[0])
    if point[0]<0 or point[0]>=n or point[1]<0 or point[1]>=m:
        return False
    elif maps[point[0]][point[1]]==1:
        return True
    else:
        return False

def solution(maps):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    q=deque()
    q.append((0,0)) 
    while q:
        cur_pt = q.popleft()
        for i in range(4):
            next_pt = cur_pt[0]+dx[i], cur_pt[1]+dy[i]
            if is_valid(next_pt, maps):
                maps[next_pt[0]][next_pt[1]]+=maps[cur_pt[0]][cur_pt[1]]
                q.append(next_pt)
    
    answer = maps[-1][-1]
    if answer<=1:
        return -1
    else:
        return answer
    


# 2. 내 답 DFS(실패)
def is_valid(point,maps):
    n=len(maps)
    m=len(maps[0])
    if point[0]<0 or point[0]>=n or point[1]<0 or point[1]>=m:
        return False
    elif maps[point[0]][point[1]]==1:
        return True
    else:
        return False

def dfs_search(point,maps):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    for i in range(4):
        next_point = point[0]+dx[i], point[1]+dy[i]
        if is_valid(next_point,maps):
            maps[next_point[0]][next_point[1]]+=maps[point[0]][point[1]]
            dfs_search(next_point,maps)

def solution(maps):
    start_point = (0,0)
    dfs_search(start_point, maps)
    print(maps)
    answer = maps[-1][-1]
    if answer<=1:
        return -1
    else:
        return answer
    
