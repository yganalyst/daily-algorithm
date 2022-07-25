"""
20220725

- No.: 1920
- type: 자료구조, 이분탐색
- Problem : 
    N개의 정수들 안에 M개의 정수가 각각 포함되어 있는지 확인하기

*문제에 제시된 변수의 범위가 매우 크기때문에, 이진탐색을 이용해야함

"""

N = int(input())
N_ls = list(map(int,input().split()))

M = int(input())
M_ls = list(map(int,input().split()))

# 1. 이분탐색방법
N_ls_sort = sorted(N_ls)
def binary_search(array,target,start,end):
    while start<=end:
        mid = (start+end)//2
        if array[mid]==target:
            return True
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return False

for i in M_ls:
    result = binary_search(N_ls_sort,i,0,len(N_ls)-1)
    if result:
        print(1)
    else:
        print(0)


# 2. 자료구조 이용 (시간초과 걸림)    
for i in M_ls:
    if i in N_ls:
        print(1)
    else:
        print(0)
    