"""
20220704 한수

- No.: 1065
- type: brute force
- Problem : 1~N개의 정수 중 한수(각 자리가 등차수열) 구하기

*나올수있는 조건을 좀 더 생각하고 구현하기
*1~99는 등차수열로 봄
*str도 iterable 객체이므로 map에 바로 들어갈 수 있음
*나머지를 이용한 방법 참고

ex)
input:
    110
output: 
    99

"""

# solve
N=int(input())
cnt=0
for i in range(1,N+1):
    if i > 99:
        i=100
        num = list(map(int,str(i)))
        st_ = set()
        for j in range(len(num)-1):
            st_.add(num[j+1]-num[j])
        if len(st_)==1:
            cnt+=1
    else:
        cnt+=1
print(cnt)

# reference
def Hansu(N):
    cnt=0
    if N<100:
        return N
    else:
        for i in range(100,N+1):
            n100 = i//100
            n10 = (i%100)//10
            n1 = i%10
            if (n100-n10)==(n10-n1):
                cnt+=1
        return 99+cnt
Hansu(int(input()))



