"""
This is a demo task.
Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
Given A = [1, 2, 3], the function should return 4.
Given A = [−1, −3], the function should return 1.
Write an efficient algorithm for the following assumptions:
N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].

- set으로 unique하게, 0이상인 것만 추리는 건 좋음
- 하지만 아래 첫 답변의 경우 max(a1)에 따라 최악의 경우가 K로 더 높음
- 하지만 Loop를 돌면, N(A 배열 개수)로 한정되기 때문에 최악의 상황을 항상 면할 수 있게 됨

"""

# 참고함
def solution(A):
    a1 = set(x for x in A if x > 0)
    if not a1:
        return 1
    n=1
    while True:
        if n not in a1:
            return n
        n+=1

# 첫 답변
def solution(A):
    a1 = set(x for x in A if x > 0)
    if not a1:
        return 1
    a2 = set(i for i in range(1, max(a1) + 2))
    return min(a2 - a1)