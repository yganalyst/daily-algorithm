"""
 - 정렬 - 삽입정렬

*데이터가 어느정도 정렬되어 있을때 훨씬 효율적


"""

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):  # i부터 0까지 -1씩 감소
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 종료 
            break
print(array)