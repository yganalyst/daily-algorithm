"""
20220702

- No.: 10870
- type: 수학,구현,재귀
- Problem : 피보나치 수열

*재귀함수 사용하기

"""

# solve 1
n = int(input())
ls_ = [0,1]
if n<2:
    print(ls_[n])
else:
    for i in range(2,n+1):
        ls_.append(sum(ls_[-2:]))
    print(ls_[-1])

# reference
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
print(fib(int(input())))