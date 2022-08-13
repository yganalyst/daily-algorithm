"""
 - 두 배열의 원소 교체
 - type : 정렬
 - problem : 
     N개 원소를 가진 두 배열 A,B
     A원소 1개와 B원소 1개를 골라 바꿔치기를 K번 할 수 있음
     최종 A의 원소의 합이 최대가 되도록하고, 최대값을 출력
    
*오름차순, 내림차순 정렬했으면 인덱스 1개씩 비교하는건 합리적임
*그러나 그냥 바꿔버리는 건 안됨 주의..
*하나씩 비교해서 A보다 B가 클 경우만 교체해야함
     
"""

N,K=map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A = sorted(A)
B = sorted(B, reverse=True)

for i in range(K):
    if A[i]<B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break    
print(sum(A))
