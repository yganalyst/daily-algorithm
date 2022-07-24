"""
 - 떡볶이 떡 만들기
 - type : 이진탐색
 - problem :
     N개의 가래떡이 있고 손님은 길이 M만큼 가래떡이 필요.
     가래떡은 높이 H인 절단기로 나란히 절단됨
     M만큼의 떡을 얻기 위한 절단기 높이 H의 최대값구하기

*순차탐색을 하면서 H를 증가시킬 순 있지만, 
*변수의 범위가 매우 크기때문에, case에 따라 불가능함
*이럴땐 이진탐색으로 접근
*mid의 값의 갱신은 잘려진 떡 길이의 합과 M으로 비교해야함
 
"""
# 1. 이진 탐색 활용 (범위가 크기 때문에)
N,M = 4,6
array = [19,15,10,17]

start = 0
end = max(array)

result = 0
while (start<=end):
    total = 0
    mid = (start+end)//2
    for x in array:
        if x > mid:
            total += x-mid
    if total < M:  # 잘려진 합이 목표값보다 낮으므로, 더 밑에서 짤라야함
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)


# 2. 순차탐색 방법 (이렇게 하면 안돼)
# N,M = 4,6
# ls_ = [19,15,10,17]
# ls_rest = [0]*4
# def cut_ricecake(H, ls_,ls_rest):
#     ls_cop = ls_[:]
#     ls_rest_cop = ls_rest[:]
#     for i in range(len(ls_cop)):
#         cut_ = ls_cop[i]-H
#         if cut_>0:
#             ls_cop[i]=H
#             ls_rest_cop[i]=cut_
#         else:
#             ls_rest_cop[i]=0
#     return ls_cop, ls_rest_cop
    
# H=0
# max_H = 0
# while H<max(ls_):
#     ls_rt, ls_rest_rt = cut_ricecake(H, ls_, ls_rest)
#     if sum(ls_rt)==M or sum(ls_rest_rt)==M:
#         max_H = H
#     H+=1
# print(max_H)
        
