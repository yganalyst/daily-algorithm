"""
 - 예제 3-1 거스름돈
 - problem : 
     500원,100원,50원,10원짜리 동전 무한히 존재
     거스름돈이 N원일 때, 최소 동전 개수 구하기
     (단 N은 항상 10의 배수)

*빼지말고 나머지로 간단하게 수정 가능
*시간복잡도 : O(K) , K는 동전의 수, N과는 무관
"""

# solve
N=1260
cnt=0
for i in [500,100,50,10]:
    num_ = N//i
    N=N-num_*i
    cnt+=num_
print(cnt)

# reference
N=1260
cnt=0
for i in [500,100,50,10]:
    cnt += N//i
    N%=i
print(cnt)    


