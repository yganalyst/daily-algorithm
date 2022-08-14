"""
 - 기출: 문자열 뒤집기
 - type : 그리디
 - problem : 
     이진(0,1)문자열이 주어졌을때, 숫자를 뒤집어서 하나로 통일하는 최소 횟수
     ex) 0001100 이면, 4~5번째 11을 00으로 뒤집으면 됨 (1번만에 가능)

*결국 처음부터 하나씩 그리디하게 서칭하면서 0과 1로 바뀌는 순간이 언제인지 count
*count한 두 수중 작은 경우를 출력하면 되는 것임
*reference보다 내 코드가 더 간결해보이는데, 고려가 안된 case가 있으려나..
"""

ls_ = [0,0,0,1,1,0,0]
cnt=ls_[0]
result=[cnt]
for i in ls_[1:]:
    if i!=cnt:
        cnt=i
        result.append(cnt)

print(min(sum(result), (len(result)-sum(result))))


# reference (책풀이) 
ls_ = [0,0,0,1,1,0,0]
cnt0 = 0  # 0으로 통일하는 경우
cnt1 = 0  # 1로 통일하는 경우

if ls_[0] == 1:
    cnt0 += 1
else:
    cnt1 += 1

for i in range(len(ls_) - 1):
    # 다음 수가 현재랑 달라지는 경우만 체크
    if ls_[i] != ls_[i + 1]:
        # 다음 수가 1인 경우
        if ls_[i + 1] == 1:
            cnt0 += 1
        # 다음 수가 1인 경우
        else:
            cnt1 += 1
print(min(cnt0, cnt1))