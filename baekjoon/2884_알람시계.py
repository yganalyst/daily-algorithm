"""
20220701

- No.: 2884
- type: 수학, 사칙연산
- Problem : 45분 전 시간 출력

*조건문 대신 수학으로 접근하기
*음수의 몫(//), 나머지(%) 계산 주의
*https://sondho.tistory.com/7

"""

# solve 1
H, M = map(int,input().split())
ch_ = M-45
if ch_<0:
    new_H = H-1
    new_M = 60+ch_
else:
    new_H = H
    new_M = ch_
if new_H<0:
    new_H=23
print(new_H,new_M)

# reference
H, M = map(int,input().split())
new_H = (H+(M-45)//60)%24
new_M = (M-45)%60
print(new_H,new_M)