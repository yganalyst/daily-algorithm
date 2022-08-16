"""
 - 기출: 볼링공 고르기
 - type : 그리디
 - problem : 
     N개의 볼링공이 1~M(자연수)인 무게를 갖고 있음
     서로 무게가 다른 볼링공 2개를 고르는 모든 조합??
     N=5, M=3, [1,3,2,3,2]
     
     (1번,2번), (1번,3번), (1번,4번), (1번,5번),
     (2번,3번), (2번,5번),
     (3번,4번)
     (4번,5번)

* 1. 2중 for 문으로 해결하는 방법
* 2. 조합으로 생각하는 방법
    - 각 무게의 중복개수 카운트
    - 경우의 수 : 각 무게별로 -> (무게 i의 수 x 무게 i 를 제외한 볼링공 수)    

*아이디어는 동일하게 풀긴했으나 (조합으로 생각)
*원래 생각했던 2중 for문 구현하는 방법(떠오르지 않았음)과 개선된 코드를 참고하면 더 잘 짤 수 있음
*ref : https://ssssol.tistory.com/53
"""

n, m = map(int, input().split())
ls_ = list(map(int, input().split()))

## 조합으로 생각하는 방법 (시간복잡도 : O(N))
check=ls_[0]
cur_s = 1
result=0
for i in range(1,n):
    if ls_[i]==check:
        cur_s+=1
        continue
    else:
        result+=cur_s*len(ls_[i:])
        cur_s=1
        check=ls_[i]    
print(result)    


## 조합으로 생각하는 방법 - 코드 개선 (시간복잡도 : O(M))
array=[0]*11
for x in ls_:
    array[x]+=1

result=0
# 무게별로 for문돌면 끝
for i in range(1,m):
    i=1
    n -= array[i]         # 무게 i 를 제외한 볼링공 수
    result += array[i]*n  # 무게 i의 수 x 무게 i 를 제외한 볼링공 수
print(result)



## 2중 for문 방법
result=0
for i in range(n):
    for j in range(i,n):
        print(ls_[i],ls_[j])
        if ls_[i]!=ls_[j]:
            result+=1
print(result)    
