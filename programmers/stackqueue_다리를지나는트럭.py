"""
20221021

- 다리를 지나는 트럭
- type: 스택/큐
- Problem : 
    https://school.programmers.co.kr/learn/courses/30/lessons/42583
    
주의할점
  - 어려웠다. 다리에 대한 2중 리스트를 만들 생각은 했지만, 범위 1~10,000이라 안했는데 되나보다..
  - 다른 여러가지 방법을 시도했지만 실패
      - global_time = bridge_length*len(truck_weights) + 1
      - 위와 같이 global time(무조건 1대씩만 건너는 경우)을 정의하고
      - 동시에 건널 경우에 대해 감축되는 시간을 게산해보고자 했었음
      - 하지만 앞의 queue가 빠져나가면 다시 진입할 수 있기 때문에 결국 bridge 단으로 식별해야할 듯
  - Reference : 다리를 queue로 두고, 비어 있을때까지 while문
      - 앞 칸 꺼내고
      - 트럭하나가 들어갈 수 있으면 대입
      - 못들어가면 0을 대입
      - 시간 +1
      - 반복 
      
*Referece
https://velog.io/@henrynoowah/PYTHON-Programmers-%EB%8B%A4%EB%A6%AC%EB%A5%BC-%EC%A7%80%EB%82%98%EB%8A%94-%ED%8A%B8

"""

# 1.Reference
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for _ in range(bridge_length)]
    while bridge:        
        bridge.pop(0)        
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:            
                t = truck_weights.pop(0)
                bridge.append(t)
            else:
                bridge.append(0)
        answer += 1
    return answer
    