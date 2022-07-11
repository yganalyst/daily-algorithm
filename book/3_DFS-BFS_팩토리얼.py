"""
 - 재귀함수 (Recursive Function) - 팩토리얼
 - type : DFS/BFS


"""
def factorial_iterative(n):
    result=1
    for i in range(1, n+1):
        result*=i
    return result

def factorial_recursive(n):
    if n<=1:
        return 1
    return n*factorial_recursive(n-1)

print(factorial_iterative(5))
print(factorial_recursive(5))