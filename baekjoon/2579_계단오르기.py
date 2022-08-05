"""
20220805 계단 오르기

- No.: 2579
- type: 다이나믹 프로그래밍
- Problem :
    계단에는 점수가 쓰여있고 도착지까지 오르면서 총 점수 최대화하기
    1. 계단은 한번에 1개 or 2개씩 오를 수 있음
    2. 연속된 세개의 계단을 모두 밟으면 안됨 (시작점 포함 X)
    3. 도착계단은 무조건 밟아야함

*현재 칸은 이전에 어떤 계단에서 올 수 있는지를 경우의 수로 생각하면 됨
*5번째 칸 : 2번째 -> 4번째에서 왔거나, 3번째에서 왔거나
*따라서 점화식은 d[i] = array[i] + max(d[i-3]+array[i-1], d[i-2])

*원래 아이디어 틀림 :
    i-1값이 연속되어 온 경우(i-2), i-1값이 연속되어 오지 않은 경우(max(i-1,i-2))
    d[i-3]으로 하는 대신 d[i-1]을 두개의 경우로 분할하려고 의도했음
    그러나, 바로 이전값이 연속되어 왔으면 그냥 i-2로만 가는게 문제임
    (연속되어 오건 안오건, 올 수 있는 경우는 위 점화식의 두가지이기 때문에 이 둘을 항상 비교해줘야함)
"""

n=int(input())
array=[]
for _ in range(n):
    array.append(int(input()))

if n==1:
    print(array[0])
elif n==2:
    print(array[1]+array[0])
else:    
    d=[0]*n
    d[0]=array[0]
    d[1]=array[1]+array[0]        
    d[2]=array[2]+max(array[1],array[0]) 
    
    for i in range(3,n):
        d[i]=array[i]+ max(d[i-3]+array[i-1], d[i-2])
    print(d[n-1])
    
    # # 틀렸음(기존아이디어)
    # d=[0]*n
    # d[0]=array[0],0
    # d[1]=array[1]+array[0],1        
    # ls_ = [array[0],array[1]]
    # max_idx = ls_.index(max(ls_))
    # d[2]=array[2]+ls_[max_idx],max_idx
    
    # for i in range(3,n):
    #     if d[i-1][1]!=1:     # 바로 이전 값이 연속되어오지 않았으면 최대값 계산
    #         ls_ = [d[i-2],d[i-1]]
    #         max_idx = ls_.index(max(ls_,key=lambda x : x[0]))
    #         d[i]=array[i]+ls_[max_idx][0],max_idx
    #     else:  # 연속되어왔으면 그냥 2개 이전걸로
            
    #         d[i]=array[i]+d[i-2][0],0
    
    # print(d[n-1][0])



