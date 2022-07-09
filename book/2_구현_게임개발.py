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
grid_size = 4,4
start, head = (1,1),0
grid_map = [[1,1,1,1],
            [1,0,0,1],
            [1,1,0,1],
            [1,1,1,1]]
step_ = [0,3,2,1]

def is_valid(point):
    if (start[0]>=0) & (start[1]>=0) & \
        (start[0]<=grid_size[1]) & (start[1]<=grid_size[1]):
        return True        
    if grid_map[start[0]][start[1]]==0:
        return True

while True:
    now_step_idx = step_.index(head)
    for i in range(1,5):
        i=1
        next_step_idx = (now_step_idx+i)%4
        print(step_[next_step_idx])
        head = step_[next_step_idx]
