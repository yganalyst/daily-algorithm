"""
 - 시각
 - type : 구현
 - problem : 
     00시 00분 00초 ~ N시 59분 59초 사이에
     3이 포함되는 모든 경우의 수

*경우의수를 한번에 뽑아버리려고 for문 하나 줄였음
*이럴땐 그냥 직관적으로 짜버리는게 좋을듯(3중으로)
     
"""

N=int(input())
total = 60*60*(N+1)
hour_cnt=0
for i in range(N+1):
    if "3" not in str(i):
        hour_cnt+=1
min_cnt=0
for i in range(60):
    if "3" not in str(i):
        min_cnt+=1
print(total - min_cnt*min_cnt*hour_cnt)


# reference
N=int(input())
cnt=0
for h in range(N+1):
    for m in range(60):
        for s in range(60):
            if "3" in str(h)+str(m)+str(s):
                cnt+=1
print(cnt)