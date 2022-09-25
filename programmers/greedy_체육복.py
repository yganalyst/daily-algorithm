"""
20220704

- 체육복
- type: 그리디
- Problem : 
    n명의 학생 중 체육복을 빌려서 체육수업을 들을 수 있는 최대 학생 수
     - 체육복 없는 학생 배열(lost)
     - 여벌 체육복 있는 학생 배열(reserve)
    단,  체육복이 없는 학생은 앞 뒤번호 학생에게만 빌릴 수 있음
    단, 여벌 체육복이 있는 학생이 도난 당할 수 있음 (빌려줄수 없게됨)

*여벌있고 도난당한 경우를 미리 제외해야하는 것 주의!

"""

def solution(n, lost, reserve):
    lost_new =list(set(lost)-set(reserve))
    reserve_new = list(set(reserve)-set(lost))
    for i in reserve_new:
        for j in lost_new:
            if abs(i-j)<=1:
                lost_new.remove(j)    
    answer = n-len(lost_new)
    return answer