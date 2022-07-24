"""
 - 부품찾기
 - type : 이진탐색
 - problem :
     N개의 부품 리스트 존재
     M개의 부품 리스트가 위 N개 리스트에 존재하는지 각각 확인

*이진탐색, 계수정렬, 자료구조를 이용한 방법     

"""

N=5
ls_exist=[8,3,7,9,2]
M=3
ls_cus=[5,7,9]

# 1. 자료구조(간단한 방법)
for i in ls_cus:
    if i in ls_exist:
        print("yes", end=' ')
    else:
        print("no", end=' ')
        
# 2. 이진탐색 (반복문)
def binary_search_iter(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid]==target:
            return target
        elif array[mid]>target:
            end = mid-1
        else:
            start = mid+1
    return None

ls_exist_sort = sorted(ls_exist)
for i in ls_cus:
    result = binary_search_iter(ls_exist_sort, i, 0, len(ls_exist)-1)
    if result==None:
        print("no", end=' ')
    else:
        print("yes", end=' ')

# 3. 계수정렬
total_array = [0]*1000001
for i in ls_exist:
    total_array[i]=1
    
for i in ls_cus:
    if total_array[i]==1:
        print("yes", end=' ')
    else:
        print("no", end=' ')
