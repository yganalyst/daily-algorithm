"""
20220824

- 무지의 먹방라이브
- type: 그리디
- Problem : 

    
*기존 아이디어 (완전탐색 방식) : 
    food_times의 각 객체를 반복해서 인덱싱하고 1씩 감소시킴
    0이되면 pass
    감소시킨 횟수와 k값이 같아지면 현재 인덱스를 저장하고 종료
    
*참고한 아이디어(이코테) :
    1. heapq에 음식별 필요한 시간으로 push하고, 제일 적게 걸리는 음식을 꺼냄
    2. 해당 음식을 모두 처리하는데 걸리는 시간으로, 나머지 음식들도 일괄처리
        - 현재 음식의 일괄처리 시간 = (현재 음식 시간 - 이전 음식 시간)*음식 수
    3. 남은시간을 봤을때 일괄처리를 못할떄까지 1,2를 반복
    4. 남은 음식들은 다시 번호를 기준으로 정렬
    5. 남은 시간 + 1번째 음식의 번호를 출력 (나머지 값 이용)
    
"""

food_times=[8,4,6,3]
k=15


# Reference (이코테)
import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    hq = []
    for i in range(len(food_times)):
        heapq.heappush(hq, (food_times[i], i+1))
    
    sum_values = 0   # 먹기 위해 사용한 시간
    previous = 0     # 직전에 다 먹은 음식 시간
    length = len(food_times) # 남은 음식의 개수
    
    while True:
        # sum_values + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
        if sum_values + (hq[0][0] - previous) * length >= k:
            break
        now = heapq.heappop(hq)
        sum_values += (now[0]-previous)*length
        length -= 1   # 다먹은 음식 제외
        previous = now[0]  # 이전 음식 시간 재설정
        
    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    hq.sort(key = lambda x: x[1]) # 번호를 기준으로 정렬
    k -= sum_values
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
