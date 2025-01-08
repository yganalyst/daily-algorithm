"""
20221217

- Brackets
- type: Stacks and Queues
- level: Easy
- Problem : 
    https://app.codility.com/programmers/lessons/7-stacks_and_queues/brackets/

*주의할점

   - 문자열 훑으면서 그거에 따라 닫히는 괄호를 FIFO 형태로 빼줘야 하기 때문에,
   - stack 구조 이용해야함
   - 예외 케이스 주의해야함
     -'((((((((' : 닫히는게 없는 경우
     -')(' : 처음부터 열리는 경우
     -'(([[]]' : 다 훑고 난 뒤에 '))' 가 더 나오면 성공인데 안나온경우 -> stack에 남아있음

*Referece

"""

# 1. 내 답 (100%)
def solution(S):

    str_dict = {"(":")", "{":"}", "[":"]"}
    close_ls = []
    for i in S:
        if i in str_dict.keys():
            close_ls.append(str_dict[i])
            continue
        elif close_ls:
            close_s = close_ls.pop()
            if close_s!=i:
                return 0
        else:
            return 0

    if close_ls:
        return 0
    return 1

# 2. 내 답 (20250106) - 100%이지만 효율성은 60%
def solution(S):
    while True:
        if "()" in S:
            S = S.replace("()","")
        elif "{}" in S:
            S = S.replace("{}","")
        elif "[]" in S:
            S = S.replace("[]","")
        else:
            break
    if S:
        return 0
    return 1

