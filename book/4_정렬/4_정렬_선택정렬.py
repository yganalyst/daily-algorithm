"""
 - 정렬 - 선택정렬

*i : 가장 작은 원소를 넣을 인덱스
*j : i 다음 인덱스들을 순회하면서 가장 작은 min_index를 도출
*i와 min_index를 스와팡
*이걸 반복하면 오름차순정렬 완료 
"""

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index=j
    array[i],array[min_index] = array[min_index],array[i]
print(array)
