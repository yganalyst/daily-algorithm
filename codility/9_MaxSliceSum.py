"""
20221217

- MaxSliceSum
- type: Maximum slice problem
- level: Easy
- Problem : 
    https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_slice_sum/

*주의할점
  - 모든 case를 고려해야하는게 아니였음
  - max sum 이므로 sum값이 음수가 아니라면 계속 범위를 확장해주면 된다.
  - 여러가지 Pair를 따질 필요 없고, 0~확장 하면서 max값만 저장하면 된다.
  - 즉 2가지만 고려하면 된다.
    - 현재 cum_sum이 음수이면, 0으로 초기화(다음 index부터 범위 다시)
    - 현재 cum_sum이 양수이면, 계속 증가
    예를들어,
      [3,-1,-1,-1,-1,3,3,3,3] 이라면 뒤의 3부터 4개만 더하는게 제일 크고
      [3,-1,-1,3,3,3,3] 이라면, 모든 범위가 앞의 3-2까지 더해져 더 커진다.
      즉, 확장 하면서 0보다 작아지는지만 확인하고 갱신해주면 됨

*Referece
https://algoisanswer.tistory.com/54

"""
# 1. Reference - O(N)
def solution(A):
    # write your code in Python 3.6
    maxSum = -float('inf')
    cum_sum = 0
    for a in A:
        cum_sum += a
        maxSum = max(maxSum, cum_sum)
        cum_sum = max(0, cum_sum)
    return maxSum


# 2. 내 답  - O(N**3)
def solution(A):
    save_ls = []
    cum_sum = 0
    for a in A:
        cum_sum +=a
        save_ls.append(cum_sum)

    n=len(A)
    answer=-2147483648
    for i in range(n):
        for j in range(i,n):
            if i==j:
                value = A[i]
            else:
                value = save_ls[j]-save_ls[i]+A[i]
            answer = max(value, answer)

    return answer

