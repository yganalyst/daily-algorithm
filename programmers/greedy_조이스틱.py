"""
20221024

- 조이스틱
- Level : 2
- type: 스택/큐
- Problem : 
    https://school.programmers.co.kr/learn/courses/30/lessons/42860
    
주의할점
  - 어렵다
  - 

*Referece
    https://alreadyusedadress.tistory.com/211

"""

# 1. 기존 내답 (틀림)
def solution(name):
    idx=0
    answer = 0
    name = list(name)
    while True:
        # 특정문자 바꾸기
        if name[idx]!="A":
            cnt_1 = min(ord(name[idx])-ord("A"), ord("Z") - ord(name[idx])+1)
            answer += cnt_1
            name[idx]="A"
        if all([i=="A" for i in name]):
            break
        
        # 이동
        n_right=1
        while True:
            if name[(idx+n_right)%len(name)] != "A":
                break
            n_right+=1      

        n_left=1
        while True:
            if name[(idx-n_left)%len(name)] != "A":
                break
            n_left+=1    
            
        if n_left < n_right:
            answer+=n_left
            idx -= n_left
        else:
            answer+=n_right
            idx += n_right
    return answer

