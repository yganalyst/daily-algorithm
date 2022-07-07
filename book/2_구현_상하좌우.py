"""
 - 상하좌우
 - type : 구현
 - problem : 
     NxN grid network
     왼쪽 위 가장자리(1,1) 에서 시작
     주어진 이동 지시에 따라 이동하고 최종 좌표 출력
     단, grid를 넘어가면 무시

     
"""

N=int(input())
path=input().split(" ")
start=[1,1]

def is_valid(value):
    return (value >= 1) & (value <= N)
        
for p in path:
    if (p=="L") & is_valid(start[1]-1):
        start[1]-=1            
    elif (p=="R") & is_valid(start[1]+1):
        start[1]+=1
    elif (p=="U") & is_valid(start[0]-1):
        start[0]-=1
    elif (p=="D") & is_valid(start[0]+1):
        start[0]+=1
print(start)    

