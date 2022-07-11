"""
 - 재귀함수 (Recursive Function)
 - type : DFS/BFS

"""

def recursive_function():
    print("재귀함수를 호출합니다")
    recursive_function()

recursive_function() # 재귀호출 제한에 걸림

def recursive_function(i):
    if i==100:
        return
    print(i, '번째 재귀 함수에서', i+1, "번째 재귀 함수를 호출합니다.")
    recursive_function(i+1)
    # 1을 넣으면 1,2,...,99까지 실행을 한 후에야 이 출력문이 실행되기 시작. => 스택 자료구조와 동일
    print(i, "번째 재귀 함수를 종료합니다")  

recursive_function(1) # 
