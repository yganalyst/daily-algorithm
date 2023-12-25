"""
20221218

- CountDistinctSlices
- type: Caterpillar method
- level: Easy
- Problem : 
    https://app.codility.com/programmers/lessons/15-caterpillar_method/count_distinct_slices/

*주의할점
  - Caterpillar method를 이해하고 풀어야함, reading 자료참고
  - 연산 규칙, 결국 범위를 넓혀감에 따라 내부 부분집합은 1, 1+2, 1+2+3 형태로 증가
     *결국 범위확장에 따라 그 범위의 길이만큼 추가되는 것임 (0,0) (0,1) (0,2)
  - 추가로, (0,3)이 distinct하면, 부분집합도 모두 distinct함
  Reference
   - 확장하는 머리부분을 front, 꼬리부분을 back으로 정의
   - front 먼저 distinct한 slice까지 넓히고, back을 하나씩 떙겨옴
     *이렇게하면 모든 경우의수 가능 (땡기면서, 중복을 지난 후의 경우를 카운트)
   - appearance를 이용해서 disticnt여부 식별해주고, back을 땡길때마다 다시 갱신해줌

  
*생각한 Test case
  - 
  
*Referece
https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=alwlren_00&logNo=221636715956
"""

# 1. Reference 
M,A=(6, [3, 4, 5, 5, 2])
def solution(M, A):
    appearance = [False] * (M + 1)
    N = len(A)
    front = 0 
    slices = 0
    for back in range(N):
        # back=2
        while front < N and appearance[A[front]] == 0:
            print(back,front)
            appearance[A[front]] += 1
            slices += front - back +1
            front += 1
        print(appearance)
        appearance[A[back]] -= 1
        print(appearance)
        print()
        if slices >= 1000000000: return 1000000000
    return slices


# 2. 내 답 - 연산 규칙은 찾아냈으나 disticnt 판단과 갱신해주는 구현 실패..
def solution(M, A):
    n=len(A)
    answer=0
    cum_sum=1
    add_n=2
    for i in range(n-1):
        if A[i]!=A[i+1]:
            cum_sum += add_n
            add_n+=1
        else:
            answer+=cum_sum
            cum_sum=1
            add_n=2
    answer+=cum_sum
    return answer

# 3. 내 답 (Performance 40%) - O(N * (N + M))
def solution(M, A):
    answer=0
    n=len(A)
    for i in range(n):
        for j in range(i,n):
            sub = A[i:j+1]
            if len(sub) == len(set(sub)):
                answer+=1
            else:
                break
    if answer > 1000000000:
        return 1000000000
    return answer