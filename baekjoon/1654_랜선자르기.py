"""
20220725

- No.: 1654
- type: 이분탐색, 매개변수탐색
- Problem : 
    K개의 길이가 다른 랜선을 잘라, 길이가 동일한 N개의 랜선을 만들어야함
    N개가 되는 최대 랜선의 길이를 구하기.
    (한번 자른 랜선은 다시 붙일 수 없음)

*기존 생각 : cutting == N이 되는 mid지점을 찾고,
            mid에서 1씩 증가시키다가 N이 줄어드는 경우 바로 직전의 mid값을 호출
            -> cutting==N인 경우가 많아서 시간초과 나는 듯
*조건을 두개만 주고(>=N or <N) start와 end가 교차될때까지해야함
*그러다보면 mid가 11->12로 넘어가는 시점에 end=mid-1이므로 end를 출력해야 최댓값임
*아래 블로그를 보고 제대로 이해함
*https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-1654-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%9E%9C%EC%84%A0-%EC%9E%90%EB%A5%B4%EA%B8%B0-%EC%8B%A4%EB%B2%843-%EC%9D%B4%EB%B6%84-%ED%83%90%EC%83%89

"""
# test case
# 4 11
# 899,799,499,539

K,N = map(int,input().split())
ls_=[]
for _ in range(K):
    ls_.append(int(input()))

def cutting(mid_):
    result=0
    for i in ls_:
        result+=i//mid_
    return result

start = 1
end = max(ls_)
while start<=end:
    mid = (start+end)//2
    cut_ = cutting(mid)
    # print(start,mid,end,cut_)
    if cut_<N:
        end=mid-1
    else:
        start=mid+1
print(end)

