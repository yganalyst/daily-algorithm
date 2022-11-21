"""
20221121

2022 KAKAO BLIND RECRUITMENT

1. 신고결과 받기
- Problem : 
    https://school.programmers.co.kr/learn/courses/30/lessons/92334    

주의할점
    효율적이고 꺠끗하게 짜자..
    1. 애초에 set(report)로 중복신고는 없어짐
    2. collections 모듈의 defaultdict를 이용하면 불필요한 loop를 줄일 수 있음
      - 초기 value값 설정가능
    개인적인 생각으로는 문제 설정에서 report는 1~200,000이고 id_list는 2~1,000이므로
    report의 loop는 1번만 쓰는 것이 최악의 효율성을 방지할 것임 (2번 답안이 좋음)


*Referece
https://velog.io/@stella317/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%8B%A0%EA%B3%A0-%EA%B2%B0%EA%B3%BC-%EB%B0%9B%EA%B8%B0Python
https://suminig.tistory.com/11

"""

# 1. 내 답
from collections import Counter
def solution(id_list, report, k):
    dict_ = {}
    for _id in id_list:
        dict_[_id] = set()
    for rep in report:
        id_usr, rep_usr = rep.split(" ")
        dict_[id_usr].add(rep_usr)
    
    req_user = Counter([i for sub in dict_.values() for i in sub])
    req_user_list = []
    for key_,value_ in req_user.items():
        if value_>=k:
            req_user_list.append(key_)
    answer=[]
    for key_,value_ in dict_.items():
        cnt=0
        for i in value_:
            if i in req_user_list:
                cnt+=1
        answer.append(cnt)
    return answer

# 2. 내 답 수정 (이게 베스트 인듯)
from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    dict_ = defaultdict(set)
    cnt_ = defaultdict(int)
    
    for rep in report:
        id_usr, rep_usr = rep.split(" ")
        dict_[id_usr].add(rep_usr)
        cnt_[rep_usr]+=1

    for i in id_list:
        count = 0
        # user가 신고한 id가 k번 이상 신고 당했으면, 받을 메일 추가
        for u in dict_[i]:
            if cnt_[u]>=k:
                count+=1
        answer.append(count)    
    return answer


        
# 2. Reference : 간단하게
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reported = {x: 0 for x in id_list} # dictionary 인라인 루프

    # 먼저 누적신고 카운트
    for r in set(report):
        a,b = r.split()
        reported[b] += 1
    
    # 누적신고 k이상인 경우에 신고를 한 유저 id에 카운트 1(결국 메일 받는 횟수임)
    for r in set(report):
        a,b = r.split()
        if reported[b] >= k:
            answer[id_list.index(a)] += 1

    return answer



