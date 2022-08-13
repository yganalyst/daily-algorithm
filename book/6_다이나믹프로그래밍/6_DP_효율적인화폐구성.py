"""
 - 효율적인 화폐 구성
 - type : 다이나믹 프로그래밍
 - problem :
     N가지 종류의 화폐를 조합해서, M원이 되도록하는 최소한의 화폐 개수
     N개의 화폐들은 얼마든지 사용할 수 있음
     불가능할 경우 -1 출력
     1<=N<=100,  1<=M<=10000

*화페가 있을때, 최소화폐금액 ~ M원까지 확인하면서 최소 화폐개수를 갱신 (bottum-up)
*화폐별 -> 금액별로 loop돌면서 최소값 갱신
*d[j-k]에 값이 있다면, 이거에 1을 더한 값 (나누어 떨어지니까)과 현재값 중 최소값으로 갱신
*2원으로 먼저 돌면서, 0원:0, 2원:1, 4원:2, 6원:3, 8원:4, 10원:5, 12원:6, 14원:7
*그다음 3원으로 갱신, 3원:1,              6원:min(3,2), 9원:3   12원:min(6,4), 15원:min(10001,5) 
"""

N,M=map(int,input().split())
array=[]
for i in range(N):
    array.append(int(input()))

d=[10001]*(M+1)
d[0]=0
for i in range(N):
    for j in range(array[i], M+1):
        if d[j-array[i]]!=10001:
            d[j]=min(d[j], d[j-array[i]]+1)

if d[M]==10001:
    print(-1)
else:
    print(d[M])