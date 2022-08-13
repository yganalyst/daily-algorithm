"""
 - 숫자 카드 게임
 - type : 그리디
 - problem : 
     NxM으로 카드에서 가장 높은 숫자를 선택하기
     단, N행을 먼저 선택 후 가장 작은 숫자 선택해야 함
     
"""

N,M = map(int,input().split(" "))
ls_=[]
for i in range(N):
    ls_.append(min(map(int,input().split(" "))))
print(max(ls_))