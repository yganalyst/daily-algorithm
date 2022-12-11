"""
20221210

- 더 맵게
- type: 힙(heap)
- level: 2
- Problem : 
    https://school.programmers.co.kr/learn/courses/30/lessons/42626
    
주의할점
  - heapq 자료구조 리뷰하고 새로 알게된 것 몇가지
    - heappush 할때 값만 해도 됨 (원래 인덱스로 했어서 했는데 없어도 된다)
    - heapify 함수 이용하면 list 한번에 push 가능 (heappush는 원소 1개씩만)
    - 이정도만 기억 (heappush, heappop, heapify)
  - 종료조건이 지저분해 졌는데 reference 참고
    1) 결국 처음 pop으로 나온 음식이 K이상이면 종료
    2) 1)에서 통과를 못했는데 queue에 아무것도 안남았다는 건 결국 못만드는 경우 (-1)

*Referece

"""

# 1. 내 답
import heapq
def solution(scoville, K):
    queue = scoville[:]
    heapq.heapify(queue)
    answer=0
    while True:
        first_v = heapq.heappop(queue)
        if first_v >= K:
            break
        if not queue:
            answer=-1
            break
        second_v = heapq.heappop(queue)
    
        new_v = first_v+(second_v*2)
        heapq.heappush(queue, new_v)
        answer+=1
                   
    return answer


# 2. Reference (동일하게 품)
import heapq as hq

def solution(scoville, K):

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1  

    return answer
