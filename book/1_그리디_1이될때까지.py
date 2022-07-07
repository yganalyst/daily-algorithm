"""
 - 1이 될 때까지
 - type : 그리디
 - problem : 
     N이 1이 될때까지 아래 두 과정 중 하나를 반복 수행하고 수행한 횟수 출력
       1. N에서 1을 뺀다
       2. N을 K로 나눈다 (나누어 떨어질때만 가능)
     
"""

N,K = map(int,input().split(" "))
cnt=0
while N!=1:    
    if N%K==0:
        N=N/K
        cnt+=1
    else:
        N-=1
        cnt+=1
print(cnt)