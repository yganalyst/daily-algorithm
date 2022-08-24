"""
20220824

- 무지의 먹방라이브
- type: 구현
- Problem : 

"""

food_times=[3,1,2]
k=5

def solution(food_times, k):
    cnt_=0
    answer=0
    while answer==0:
        for i in range(len(food_times)):
            if food_times[i]<1:
                continue
            else:
                food_times[i]-=1
                cnt_+=1    
                if cnt_==k:
                    answer=(i+1+1) % len(food_times)
                    if food_times[answer-1]==0:
                        answer=-1
                    break
    return answer

solution(food_times, k)
