"""
20221128

- 타겟 넘버
- type: DFS/BFS
- Problem : 
    https://school.programmers.co.kr/learn/courses/30/lessons/43165
    
주의할점
  - 처음에 백트래킹으로 짰는데, Tvalue가 독립적으로 안돼서 실패함 (다른 루프에도 영향을 줌)
  - 영향을 안주려면 변수로 선언하지말고, DFS 입력 파라미터를 바꿔주는 식으로 하면 됨
  - list에 저장할 필요 없고 조건 맞으면 카운트만 하면 됨( 어짜피 중복될 일이 없으므로)

*Referece

"""

# 1. 내 답 (DFS + 백트래킹)
## - 답이 뭐였는지까지 기록하려고 백트래킹을 넣은건데 이건 불필요함
import copy
result=[]
def dfs(idx, mylist,numbers,target):
    global result
    if idx==len(numbers):
        if sum(mylist) == target:
            result.append(copy.deepcopy(mylist))
            return
        else:
            return
    
    # + 하는 경우
    mylist.append(1*numbers[idx])
    dfs(idx+1,mylist,numbers,target)
    mylist.pop()

    # - 하는 경우
    mylist.append(-1*numbers[idx])
    dfs(idx+1,mylist,numbers,target)
    mylist.pop()        

def solution(numbers, target):
    global result
    n=len(numbers)
    dfs(0,[],numbers,target)
    
    answer = len(result)
    return answer

# 2. Reference 
answer = 0
def DFS(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if(idx== N and target == value):
        answer += 1
        return
    if(idx == N):
        return

    DFS(idx+1,numbers,target,value+numbers[idx])
    DFS(idx+1,numbers,target,value-numbers[idx])
def solution(numbers, target):
    global answer
    DFS(0,numbers,target,0)
    return answer
