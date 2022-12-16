"""
20221216

- MaxProductOfThree
- type: Sorting
- level: Easy
- Problem : 
    https://app.codility.com/programmers/lessons/6-sorting/max_product_of_three/

*주의할점
  - 은근 어려움
  - 경우의 수를 하나하나 따져서 풀었는데, 커버되는 간단한 식을 못찾음
  - Pos와 neg를 나눠서 생각하니까, 더 복잡해 진듯 하..
  Reference
   - 오름차순 정렬
   - 2가지 경우 중 max값으로 커버
     - 앞에서 1개 + 뒤에서 2개 => (양수1개+음수2개)
     - 뒤에서 3개 => (양수3개, 양수0개일땐 음수로 커버)

*Referece
https://sooho-kim.tistory.com/48
"""

# 1. Reference (아래 경우의 수가 2가지로 커버됨 )
def solution(A):
    A = sorted(A)
    contain_neg = A[0]*A[1]*A[-1]
    contain_pos = A[-1]*A[-2]*A[-3]
    return max(contain_neg,contain_pos)

# 2. 내 답 (100%)
def solution(A):
    
    A_pos = sorted([i for i in A if i >= 0], reverse=True)
    A_neg = sorted([i for i in A if i < 0])

    # 양수2개 + 음수 1개 밖에 없는 경우
    if len(A_pos)==2 and len(A_neg)==1:
        return A_pos[0]*A_pos[1]*A_neg[0]
    # 양수가 0개 인 경우 -> 절대값이 작은 수로 꺼내야됨
    if len(A_pos)==0:
        return A_neg[-1]*A_neg[-2]*A_neg[-3]

    cond1=0
    cond2=0
    # 양수 3개인 경우
    if len(A_pos)>=3:
        cond1 = A_pos[0]*A_pos[1]*A_pos[2]
    # 양수 1개 + 음수 2개인 경우
    if len(A_pos)>=1 and len(A_neg)>=2:
        cond2 = A_pos[0]*A_neg[0]*A_neg[1]
    return max(cond1,cond2)

