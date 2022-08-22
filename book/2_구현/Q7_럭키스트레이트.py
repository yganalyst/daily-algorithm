"""
 - 기출: 럭키 스트레이트
 - type : 구현
 - problem : 
     점수 N이 주어졌을 때, 자리수 기준으로 반으로 나누고
     좌우의 자리수 합이 같은지 확인하기
     ex) 123,402 => 6(1+2+3) + 6(4+0+2)
    단 N의 자리수(숫자의 개수)는 항상 짝수 

"""

n='7755'
cut_ = int(len(n) / 2)
forth = sum(map(int,n[:cut_]))
back = sum(map(int,n[cut_:]))
if forth == back:
    print("LUCKY")
else:
    print("READY")
