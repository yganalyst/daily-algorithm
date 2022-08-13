"""
 - 이진탐색 - 재귀, 반복문 구현

*정렬된 데이터에 대하여 시작점, 끝점, 중간점을 정의
*중간점보다 크냐 작냐에 따라 다시 3가지 지점을 수정하면서 탐색
*한번 탐색할때마다 절반씩 후보가 줄어듦
"""

# 1. 재귀 함수 이용
def binary_search_recur(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid]==target:
        return mid
    elif array[mid] > target:
        return binary_search_recur(array, target, start, mid-1)
    else:
        return binary_search_recur(array, target, mid+1, end)

# 2. 반복문 이용
def binary_search_iter(array, target, start, end):
    while start<=end:
        mid = (start+end)//2
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end = mid -1
        else:
            start = mid + 1
    return None

n,target=10,7
array = [1,3,5,7,9,11,13,15,17,19]
result = binary_search_iter(array, target, 0,n-1)
if result==None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)

