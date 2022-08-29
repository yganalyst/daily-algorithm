"""
20220824

- 무지의 먹방라이브
- type: 그리디
- Problem : 

    
*기존 아이디어 (완전탐색 방식) : 
    food_times의 각 객체를 반복해서 인덱싱하고 1씩 감소시킴
    0이되면 pass
    감소시킨 횟수와 k값이 같아지면 현재 인덱스를 저장하고 종료
    

    
"""

food_times=[3,1,2]
k=5



# Reference (이코테)
import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    hq = []
    for i in range(len(food_times)):
        heapq.heappush(hq, (food_times[i], i+1))
    
    sum_of_times = 0
    prev = 0
    length = len(food_times)
    
    while True:
        if sum_of_times + (hq[0][0] - prev) * length >= k:
            break
        now = heapq.heappop(hq)
        sum_of_times += (now[0]-prev)*length
        length -= 1
        prev = now[0]
        
    hq.sort(key = lambda x: x[1]) # 번호를 기준으로 정렬
    k -= sum_of_times
    answer = hq[k%length][1]
    return answer



# 기존 아이디어 (틀림)
def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    cnt_=0
    while cnt_!=k:
        for i in range(len(food_times)):
            if food_times[i]<1:
                continue
            else:
                food_times[i]-=1
                cnt_+=1    
                idx=i

    answer=-1
    for i in range(1,len(food_times)):
        next_idx = (idx+i) % len(food_times)
        if food_times[next_idx]==0:
            continue
        else:
            answer=next_idx+1
            break
    
    return answer

solution(food_times, k)
