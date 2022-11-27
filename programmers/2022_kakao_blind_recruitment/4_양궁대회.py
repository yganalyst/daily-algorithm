"""
20221126

2022 KAKAO BLIND RECRUITMENT

4. 양궁대회 (Level 2)
- Problem : 
    https://school.programmers.co.kr/learn/courses/30/lessons/92342

주의할점
    reference 참고 ㅠㅠ
    크게 3개의 함수로 구성
    1. 과녁판 점수뽑는 dfs함수
      - 각 과녁마다 {0개 맞추기, apeach보다 1개 더맞추기} 중 1개 선택하는 경우
      - 맞추고 다음 과녁으로 넘어감 DFS 방식
        - 다음 과녁으로 넘어갈때 남은 화살도 2가지 경우(n-info[i]-1 or n)로 나뉨
      - 0점 과녁까지 탐색이 끝나면 answer list로 판단    
    2. 어피치와 점수 비교하는 함수 2개로 구성
    3. 마지막 출력 정렬방식
      - 재귀 실행이 점수를 먹는경우 -> 안먹는 경우 순으로 코드가 구현되었기 때문에 
      - 모두다 먹는 경우가 끝나면 -> 마지막꺼부터 다시 안먹는 경우 -> 그르고 다음 과녁을 먹는 경우
      - 이 순으로 넘어감
      - 그렇기 떄문에 재귀가 진행될수록 더 멀리있는(더 작은 점수가 있는) 과녁에 도달하게 됨
      - 따라서 끝난 후에 뒤집거나 마지막꺼 출력하면 됨
    
    **백트래킹 (재귀가 끝날때 pop을 하는 이유)
    **Reference 약간의 오류 수정했음!!
      - 마지막에 화살이 남은 경우 (종료조건에서 n=0이 아닌 경우)
      - 마지막 과녁에 남은 화살을 갱신해줬는데, 그럼 기존께 누락됨 -> 누적(+=)으로 바꿈
      

*Referece
    https://yensr.tistory.com/24
    https://kjhoon0330.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%96%91%EA%B6%81%EB%8C%80%ED%9A%8C-Python

"""

n=9
info=[0,0,1,2,0,1,1,1,1,1,1]

# Reference
import copy
MAX_SCORE_DIFF = 0
answers = []
 
# 라이언과 어피치의 점수 차이를 계산하는 함수
def calcScoreDiff(info, myshots):
    enemyScore, myScore = 0, 0
    for i in range(11):
        if (info[i], myshots[i]) == (0, 0):
            continue
        if info[i] >= myshots[i]:
            enemyScore += (10 - i)
        else:
            myScore += (10 - i)
    return myScore - enemyScore
 
def dfs(info, myshots, n, i):
    global MAX_SCORE_DIFF, answers
    # 종료조건 : 마지막 과녁까지 재귀가 실행된(i=10) 다음
    if i == 11:
        
        # 마지막에 화살이 남은 경우가 있음
        if n != 0:
            myshots[10] += n


        scoreDiff = calcScoreDiff(info, myshots)
        # 어피치보다 점수가 작거나 같으면 그냥 버림 (이겨야되니까)
        if scoreDiff <= 0:
            return
        # result에 복사
        result = copy.deepcopy(myshots)
        # 최대 점수차이면 지금까지 있는거 버리고 갱신
        if scoreDiff > MAX_SCORE_DIFF:
            MAX_SCORE_DIFF = scoreDiff
            answers = [result]
            return
        # 같은 최대 점수라면 append하기
        if scoreDiff == MAX_SCORE_DIFF:
            answers.append(result)
        return
 
    # for문 대신 이렇게 감소하도록 변수에 직접 넣어줌
    # 점수 먹는 경우
    if info[i] < n:
        # 맞혀야하는 화살 = apeach가 맞힌 화살 + 1
        myshots.append(info[i] + 1)
        # 남은 화살 = n - 맞혀야하는 화살       
        dfs(info, myshots, n - info[i] - 1, i + 1)
        myshots.pop()
 
    # 점수 안먹는 경우
    # 맞혀야하는 화살 = 0
    myshots.append(0)
    # 남은 화살 = n  
    dfs(info, myshots, n, i + 1)
    myshots.pop()
 
def solution(n, info):
    global MAX_SCORE_DIFF, answers
    dfs(info, [], n, 0)
    if answers == []:
        return [-1]
    answers.sort(key = lambda x : x[::-1], reverse=True)
    return answers[0]

solution(n,info)
