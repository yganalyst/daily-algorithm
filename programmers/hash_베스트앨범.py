"""
20220925

- 베스트앨범
- type: 해시
- Level : 3
- Problem : 
    https://school.programmers.co.kr/learn/courses/30/lessons/42579

주의할점
  - 잘 풀었는데 정렬에서 조금 버벅
  - list 정렬(sorted, sort)할 때 여러 key로 멀티 정렬하는 방법이 있었다
    - sorted(list, key=lambda x : (x[0], -x[1]))
    - "-"를 붙이면 알아서 오름 또는 내림차순이 됨(reverse 불필요)
    - 괄호 쳐서 두개로 넣어주면 두개로 인식함.. 나이스..

*Referece
 https://hello-bryan.tistory.com/43
"""

# 내 답안
from collections import defaultdict
def solution(genres, plays):
    answer = []
    dict_info = defaultdict(list)
    dict_sum = defaultdict(int)

    for i in range(len(plays)):
        dict_sum[genres[i]]+=plays[i]
        dict_info[genres[i]].append((i,plays[i]))
        
    sort_genres = sorted(dict_sum.items(), key=lambda x : -x[1])
    for genre,_ in sort_genres:
        results = sorted(dict_info[genre], key=lambda x : (-x[1],x[0]))[:2]
        answer += [idx for idx,_ in results]
        
    return answer

