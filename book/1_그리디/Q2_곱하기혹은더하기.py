"""
 - 기출: 곱하기 혹은 더하기
 - type : 그리디
 - problem : 
     문자열이 주어졌을때, 왼쪽부터 오른쪽으로 하나씩 +또는 x연산하여 최대 값 계산
     0 또는 1임을 고려했을때 무조건 곱하기만 하면 안됨
     
*조건문은 2가지(새로 입력한 값, 지금까지 결과값)를 확인해야함
*2가지 중 하나가 <=1 인 경우는 +, 나머지는 x이면 됨

"""

ls_ = list(map(int,input()))

result=0
for i in ls_:
    if result<=0 or i<=1:
        result+=i
    else:
        result*=i
print(result)

