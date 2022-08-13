"""
 - 정렬 - 퀵 정렬

*피벗(pivot)을 기준으로 큰 데이터와 작은 데이터를 교환하는 방식

"""

# 1. 근본
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start+1
    right = end
    while left <= right:
        # left : pivot보다 큰 데이터를 찾을떄 까지
        while left <= end and array[left] <= array[pivot]:
            left+=1
        # right : pivot보다 작은 데이터를 찾을떄 까지
        while right > start and array[right] >= array[pivot]:
            right-=1
        if left > right: # 엇갈린 경우 : 피벗과 작은 데이터(right)를 바꾼다.
            array[right], array[pivot] = array[pivot], array[right]
        else:            # 엇갈리지 않은 경우 : 작은 데이터(right)와 큰 데이터(left)를 교체
            array[left], array[right] = array[right], array[left]
    
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)
    

# 2. 파이썬스러운 코딩
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot=array[0]
    tail=array[1:]
    
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    
    return quick_sort(left_side)+[pivot]+quick_sort(right_side)

print(quick_sort(array))
    


