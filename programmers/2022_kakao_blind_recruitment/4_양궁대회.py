"""
20221126

2022 KAKAO BLIND RECRUITMENT

4. 양궁대회 (Level 2)
- Problem : 
    https://school.programmers.co.kr/learn/courses/30/lessons/92342

주의할점
    reference 참고 ㅠㅠ    
    과녁판 점수뽑는 dfs함수, 어피치와 점수 비교하는 함수 2개로 구성
    

*Referece
    https://yensr.tistory.com/24

"""

n=5
info=[2,1,1,1,0,0,0,0,0,0,0]

# Reference
maxScore = 0		# 가장 큰 점수 차이
maxList = []		# 가장 큰 점수 차이를 낸 배열 
def ryanScore(index, score, n, apeach) :	# dfs 함수
    if n == 0 : 				# 횟수가 0 이면 calScore() 호출
        calScore(score, apeach)
        return
    
    if index == 11: return		# 0~10까지의 점수만 존재
    
    sc = apeach[index]			# 어피치가 (index)점을 맞힌 횟수
    for i in range(sc+2):		# 0부터 (index)+1까지 맞히는 경우만 고려
        if n >= i:			# n보다 크면 안되니까 고려
            score[index] = i
            ryanScore(index+1, score, n-i, apeach)
            score[index] = 0        
    
def calScore(ryan, apeach):		# 점수 계산 함수
    global maxScore, maxList
    rScore = 0	# 라이언 점수
    aScore = 0	# 어피치 점수
    
    for i in range(11):
        if ryan[i] == 0 and apeach[i] == 0: continue	# 둘다 0이면 패스
            
        if ryan[i] > apeach[i] : rScore += (10-i)	# 라이언이 더 많이 맞췄으면 점수획득
        else : aScore += (10-i)				# 아니면 어피치 점수획득
            
    if rScore > aScore :		# 라이언 점수가 더 높을 때만 고려
        diff = rScore - aScore
        if diff > maxScore:		# 최대값 갱신
            maxScore = diff
            maxList = list(ryan)
            
        elif diff == maxScore:			# 최대값이 같을 경우
            for i in range(11):	
                if ryan[-i] > maxList[-i]:	# 낮은 점수를 많이 맞은 경우가 선택
                    maxList = list(ryan)
                    break
                elif ryan[-i] < maxList[-i]:
                    break
                    
                    
def solution(n, info):
    temp = [0 for i in range(11)]
    ryanScore(0, temp, n, info)		# dfs
    
    if len(maxList)==0 : return [-1]
    else: return maxList
