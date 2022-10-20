"""
20221019

- 위장
- type: 스택/큐
- Problem : 
    https://school.programmers.co.kr/learn/courses/30/lessons/42586
    
주의할점
  - 구현은 했으나 반복문이 2~3개가 들어가는 비효율적인 코드임
      1) 구현에 소요되는 각 시간 먼저 구하기
      2) queue 처리 (이게 좀 비효울적)
  - 2)번을 보다 효율적으로 처리한 Reference
  - 애초에 시간의 업데이트로 직관적인 FIFO를 구현한 Reference 참고

*Referece
https://whwl.tistory.com/54
https://huidea.tistory.com/15

"""

progresses = [93, 30, 55]
speeds = [1, 30, 5]

# 1. 내 답 
from collections import deque
import math
def solution(progresses, speeds):
    prog_dur = deque([])
    for p,s in zip(progresses, speeds):
        duration = math.ceil((100-p) / s)
        prog_dur.append(duration)
    answer=[]
    processed = []
    while prog_dur:
        cur_q=prog_dur.popleft()
        if cur_q in processed:
            continue
        processed.append(cur_q)
        n=1
        for i in prog_dur:
            if cur_q >= i:
                n+=1
                processed.append(i)
            else:
                break
        answer.append(n)
    return answer

# 2. Reference 내 답에서 queue처리 하는 부분 효율적으로
import math
def solution(progresses, speeds):
    prog_dur = []
    for p,s in zip(progresses, speeds):
        duration = math.ceil((100-p) / s)
        prog_dur.append(duration)

    front = 0
    answer = []
    for idx in range(len(prog_dur)):
        if prog_dur[idx] > prog_dur[front]:
            # 기준값보다 커질때 차이 값으로 카운트해서 저장
            answer.append(idx - front)
            # 기준값 갱신
            front = idx 
    answer.append(len(prog_dur) - front)  
    return answer

# 3. Reference Time 업데이트로 FIFO를 바로 구현하는 코드
def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    while len(progresses) > 0:
        # 현재 time에서 배포가 가능해지면 pop으로 추출
        if (progresses[0] + time*speeds[0]) >= 100: 
            progresses.pop(0)
            speeds.pop(0)
            count += 1            
        else:
            # 배포가 안되는 경우가 생기면 지금까지 배포된 count 추가하고, 0으로 갱신
            if count > 0:
                answer.append(count)
                count = 0
            # 시간을 하루 씩 계속 업데이트
            time += 1
    answer.append(count)
    return answer