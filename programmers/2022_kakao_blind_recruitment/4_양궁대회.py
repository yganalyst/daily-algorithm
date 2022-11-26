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
    
    
    2. 어피치와 점수 비교하는 함수 2개로 구성
    
    

*Referece
    https://yensr.tistory.com/24
    https://kjhoon0330.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%96%91%EA%B6%81%EB%8C%80%ED%9A%8C-Python

"""

n=5
info=[2,1,1,1,0,0,0,0,0,0,0]

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
    if i == 11:
        if n != 0:
            myshots[10] = n
        scoreDiff = calcScoreDiff(info, myshots)
        if scoreDiff <= 0:
            return
        result = copy.deepcopy(myshots)
        if scoreDiff > MAX_SCORE_DIFF:
            MAX_SCORE_DIFF = scoreDiff
            answers = [result]
            return
        if scoreDiff == MAX_SCORE_DIFF:
            answers.append(result)
        return
 
    # 점수 먹는 경우
    print(myshots)
    if info[i] < n:
        myshots.append(info[i] + 1)
        dfs(info, myshots, n - info[i] - 1, i + 1)
        myshots.pop()
 
    # 점수 안먹는 경우
    myshots.append(0)
    dfs(info, myshots, n, i + 1)
    myshots.pop()
 
def solution(n, info):
    global MAX_SCORE_DIFF, answers
    dfs(info, [], n, 0)
    if answers == []:
        return [-1]
    answers.sort(key = lambda x : x[::-1], reverse=True)
    return answers[0]

len(answers)
