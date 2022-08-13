"""
 - 정렬 - 계수 정렬

*데이터의 범위 및 크기가 한정되어 있을때,
*데이터가 많이 중복되어 있을 수록 유리함
*0과 999,999단 두 개에의 데이터만 존재한다면, 비효율적임
* -> (1,000,000원소를 갖는 리스트를 만들어야함)

"""

array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
count = [0]*(max(array)+1)

for i in range(len(array)):
    count[array[i]]+=1
    
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
    