"""
 - 기출: 모험가길드
 - type : 그리디
 - problem : 
     N명의 모험가는 각각 공포도 X를 갖고 있음
     공포도 X인 모험가는 반드시 X명 이상의 그룹으로 구성되어야 함
     최대 그룹 수는 ?

*최소 공포도부터 그리디하게 서칭하는건 맞음
*그러나 list에서 빼고 넣고 복잡한 계산 필요 없음
*data를 모두 훑으면서 count만 갱신해주며 result(그룹 수)만 체크해주면 됨
*쉬운건데 못풀었다..
"""

n=5
p_ls = [2,3,1,2,2]
p_ls = sorted(p_ls)

result=0
count=0
for i in p_ls:
    count+=1 # 현재 그룹에 해당 모험가를 포함
    if count>=i: # 현재까지 모아진 그룹이 현재의 공포도를 넘어가면 그룹 결성
        result+=1
        count=0  # 그룹 초기화    
print(result)



