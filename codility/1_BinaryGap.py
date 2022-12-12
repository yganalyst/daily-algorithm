"""
20221212

- BinaryGap
- type: Iterations
- level: Easy
- Problem : 
        https://app.codility.com/programmers/lessons/1-iterations/
    
주의할점
  - 첫 시도에서 Gap을 구하는 것에서 좀 해맴 ..
  - binary를 만듦과 동시에 gap을 구해보자 (두번쨰 시도)

*Referece
  - 2진수는 bin 함수 이용하면 간담함.. 9의 2진수 bin(9)[2:]
  - strip과 split 함수 이용해서 1에 감싸진 "0" 리스트 반환 후 max와 len으로 카운트

"""


# 1. 내 답 (첫 시도 성공)
def solution(N):
    binary=''
    while N!=1:
        binary = str(N%2) + binary
        N//=2
    binary = "1" + binary

    cnt=0
    check=False
    answer = 0
    for s in binary:    
        if s=="1":
            if check:      # 1을 연속으로 만나는 경우
                pass
            else:
                check=True # 1을 처음 만나는 경우
                answer = max(answer,cnt)
        else:
            if check:      # 0을 처음 만나는 경우
                cnt=0
                check=False
            cnt+=1

    return answer


# 2. 다른사람 풀이 참고
def solution(N):
    binary=''
    while N!=1:
        binary = str(N%2) + binary
        N//=2
    binary = "1" + binary
    
    # binary = bin(9)[2:]   # 내장 함수 활용

    return len(max(binary.strip("0").strip("1").split("1")))
    
    # max(["0000","000"]) = "0000"