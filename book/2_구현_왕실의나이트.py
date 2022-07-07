"""
 - 왕실의 나이트
 - type : 구현
 - problem : 
     체스말이 다음 두가지 경우로 움직일 수 있음
       1. 수평 2칸 수직 1칸
       2. 수직 2칸 수평 1칸
     시작점이 주어졌을때 갈 수 있는 모든 경우의 수 구하기
     (단, 밖으로 나갈 수 없음)
 
*ord() : 문자열의 유니코드 반환해줌
     
"""

col,row = list(input())
col = list('abcdefg').index(col)+1
#col = int(ord(col)-ord('a')+1)   # 유니코드 이용한 방식
start = (col,int(row))

def is_valid(value):
    return (value>=1) & (value<=8)

cnt=0
for i in [2,-2]:
    for j in [1,-1]:
        if is_valid(start[0]+i) & is_valid(start[1]+j):
            cnt+=1
        if is_valid(start[1]+i) & is_valid(start[0]+j):
            cnt+=1
print(cnt)

