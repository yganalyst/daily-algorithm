"""
 - 게임 개발
 - type : 구현
 - problem : 
     NxM grid network 캐릭터가 지시에 따라 움직임 (방향 존재)
        1. 현재 위치와 방향을 기준으로 반시계방향으로 회전하며 갈곳을 정함
        2. 현재 방향이 가보지 않았으면 회전후 전진, 가봤으면 회전만 하고 다시 1단계로
        3. 네 방향 모두 가봤으면, 바라보는 방향을 유지한채 한 칸 뒤로가고 다시 1단계로
        (단, 뒤가 바다인 경우 움직임을 멈춤)
        0:북, 1:동, 2:남, 3:서
"""
grid_size = list(map(int,input().split()))
x,y, head = map(int,input().split())
grid_map=[]
for i in range(grid_size[0]):
    grid_map.append(list(map(int,input().split())))

start = [x,y]    
step_ = [0,3,2,1]
hist_ = []
hist_.append(start)

def is_valid(point):
    cond1,cond2,cond3 = False,False,False
    if (point[0]>=0) & (point[1]>=0) & \
        (point[0]<=grid_size[1]) & (point[1]<=grid_size[1]):
        cond1=True
    if grid_map[point[0]][point[1]]==0:
        cond2=True
    if point not in hist_:
        cond3=True
    return all([cond1,cond2,cond3])

def routing(head,point):
    point_new = point[:]
    if head==0:
        point_new[0]-=1
    elif head==1:
        point_new[1]+=1
    elif head==2:
        point_new[0]+=1
    elif head==3:
        point_new[1]-=1
    return point_new

while True:
    now_step_idx = step_.index(head)
    bl_=False
    for i in range(1,5):
        next_step_idx = (now_step_idx+i)%4
        head = step_[next_step_idx]
        next_point = routing(head, start)
        if is_valid(next_point):
            start = next_point[:]
            hist_.append(start)
            bl_=True
            break
    if not bl_:
        break
print(len(hist_))
