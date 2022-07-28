"""
 - 1로 만들기
 - type : 다이나믹 프로그래밍
 - problem :
     4개의 연산을 통해 1로 만드는데, 최소 연산 횟수 구하기
     1. 5로 나누어 떨어지면, 5로 나눈다.
     2. 3으로 나누어 떨어지면, 3으로 나눈다.
     3. 2로 나누어 떨어지면, 2로 나눈다.
     4. X에서 1을 뺀다. 
     
*bottom-up 방식으로 구현
*1부터 입력x 까지 거꾸로 올라가며 연산횟수를 저장
*d[i] : i를 1로만 드는데 최소 연산 횟수
*idea : 
    X가 3으로 나누어 떨어진다면 d[i]는 d[i//3]+1
    d[6]이 3으로 나누어 떨어진다면 연산횟수는 d[2](d[i//3])에 연산횟수를 1을 더한 것과 같음
"""

x=int(input())
d=[0]*30001  # case 범위
for i in range(2,7):
    # 일단 1을빼면 바로 이전 숫자의 최소 연산횟수가 나오고,
    d[i]=d[i-1]+1 
    # 나누어떨어질때의 숫자와 비교해서 더 작은걸 선택 최소 연산횟수로 저장
    if i%2==0:
        d[i]=min(d[i],d[i//2]+1)
    if i%3==0:
        d[i]=min(d[i],d[i//3]+1)
    if i%5==0:
        d[i]=min(d[i],d[i//5]+1)
print(d[x])