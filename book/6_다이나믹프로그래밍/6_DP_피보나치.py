"""
 - 다이나믹 프로그래밍 : 피보나치 수열

*기존 재귀함수 방식으로는 복잡도가 너무 올라감
*두개의 재귀함수를 타면서, 동일한 연산을 중복해서 계속하는 비효율 발생
*다이나믹 프로그래밍을 통해 반복적인 계산을 줄임
* 조건 :
    1. 큰 문제를 작은 문제로 나눌 수 있음
    2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일    
"""
import time    

# 1. 재귀함수 방법
def fibo(n):
    if n<=2:
        return 1
    return fibo(n-1)+fibo(n-2)


# 2. DP 방법
d=[0]*100 # Memoization을 위한 저장공간
def fibo_dp(n):
    print("f("+str(n)+")", end=' ')
    print(d)
    if n<=2:
        return 1
    if d[n]!=0:
        return d[n]
    d[n]=fibo_dp(n-1)+fibo_dp(n-2)
    return d[n]

start_time = time.time()
fibo_dp(99)
end_time = time.time()
print("running time:",round(end_time-start_time,2))
