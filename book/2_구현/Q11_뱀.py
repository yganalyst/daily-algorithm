"""
 - 기출: 뱀
 - type : 구현
 - problem : 
     뱀이 사과를 먹으면 몸이 길어지고, 벽이나 자기 몸에 부딪히면 게임이 끝난다.
     게임은 정사각 보드 NxN 위에서 진행
     처음에 길이는 1, 좌측 맨 위에서 시작,오른쪽을 향함
     다음 규칙을 따라 이동함
         1. 몸 길이를 늘려 머리를 다음칸에 위치
         2. 이동한 칸에 사과가 있다면, 먹고 꼬리는 제자리
         3. 이동한 칸에 사과가 없다면, 꼬리를 줄여서 이동한 칸으로 이동 (몸 길이는 그대로임)
     사과 위치와 이동경로가 주어질때, 이 게임이 몇초에 끝나는지 계산
     
*종료 조건 : 벽에 닿았는지, 이동하려는 칸에 자기 몸이 있는지
*식별 해야 할 것 : 시간, routing, 
그래프에 뱀이 차지하고 있는 칸이 어떤 칸들인지
     - 몸의 길이
     - tracking
"""

n=int(input())
k=int(input())

graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(k):
    a,b=map(int,input().split())
    graph[a][b]=1

L=int(input())
dir_info = []
for _ in range(L):
    x,c=input().split()
    dir_info.append((int(x),c))

def change_direction(head,nex_c):
    if nex_c=='D': # turn right
        head = (head+1)%4
    elif nex_c =="L": # turn left
        head = (head-1)%4  
    return head
    
def routing(point, head):
    if head==0:  # right
        return [point[0],point[1]+1]
    elif head==1: # down
        return [point[0]+1,point[1]]
    elif head==2: # left
        return [point[0],point[1]-1]
    elif head==3: # up
        return [point[0]-1,point[1]]

def isvalidpoint(point):
    if point[0]>=1 and point[0]<=n and point[1]>=1 and point[1]<=n:
        return True
    else:
        return False

from collections import deque

q = deque([])
head=0
loc=[1,1]
q.append(loc)
time_steps = 0
x,c = dir_info.pop(0)
while True:
    # print(q)
    time_steps+=1

    # 1. 다음 칸으로 이동    
    next_loc = routing(loc,head)

    # 2. 종료조건 확인
    #   (1) 벽에 닿았는지
    if not isvalidpoint(next_loc):
        break

    #   (2) 자기 몸이 있는지
    if next_loc in q:
        break

    # 3. 통과했으면 이동
    #    (1) 사과가 없으면 이동
    if graph[next_loc[0]][next_loc[1]]==0:
        q.popleft() 
    else:
    #    (2) 사과가 있으면 꼬리를 늘림
        graph[next_loc[0]][next_loc[1]]=0

    # 4. Queue에 이번에 이동한 칸 업데이트
    q.append(next_loc)
    loc=next_loc
        
    # 5. 이동 후 회전 방향 결정
    if time_steps==x:
        head = change_direction(head,c)
        if dir_info:
            x,c = dir_info.pop(0)
print(time_steps)


