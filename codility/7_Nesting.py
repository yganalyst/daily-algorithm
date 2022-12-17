"""
20221217

- Nesting
- type: Stacks and Queues
- level: Easy
- Problem : 
    https://app.codility.com/programmers/lessons/7-stacks_and_queues/fish/

*주의할점
   - 비어있을떄는 1로 예외처리해야함 .. 명시 좀 해주세요
   Reference
     - 원래는 stack 문제이므로, stack(FILO)을 이용
     - "("일떄만 stack에 append 하고, ")"를 만나면 pop 해주는 방식
   

*Referece
https://br-brg.tistory.com/74

"""
# 1. 내 답 (100%) - O(N)
def solution(S):
    if not S:
        return 1

    result=0
    for i in S:
        if result<0:
            return 0
        if i=="(":
            result+=1
        else:
            result-=1

    if result!=0:
        return 0
    return 1

# 2. Reference (Stack 이용) -

def solution(S):
    
    nest = {"(":")"}
    stack = []

    for s in S:
        if s in nest.keys():
            stack.append(s)
        elif s in nest.values():
            if stack:
                stack.pop()
            else:
                return 0        
    
    if not stack:
        return 1
    else:
        return 0



