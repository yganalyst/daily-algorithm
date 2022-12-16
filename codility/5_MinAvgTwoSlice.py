"""
20221216

- MinAvgTwoSlice
- type: Prefix Sums
- level: Medium
- Problem : 
    https://app.codility.com/programmers/lessons/5-prefix_sums/min_avg_two_slice/

*주의할점
   - Prefix로도 잘 안풀리고, 수학적으로 접근헤야하는 문제..
   - 기존에 푼 답은 slice 길이가 2~N까지 모두 다 해준 것임
   Reference 참고
   - reference에 따라서 slice 길이가 2일때, 3일때만 비교해 주면 됨을 증명할 수 있음
   1. slice가 2일 때
     - a < b < c < d 일 때, 
        *a < (a+b)/2 < b, *c < (c+d)/2 < d 이고, *(a+b)/2 < (c+d)/2 이므로,
        (a+b)/2 < (a+b+c+d)/4 < (c+d)/2 를 만족한다.
     - 따라서, slice 2인 경우 (연속되는 숫자 2개의 평균)만 따져주면 됨
   2. slice가 3일 때
     - (2,8,2)의 평균은  4, (2,8)의 평균은 5, (8,2)의 평균은 5 
     - 따라서 slice가 3일 때 가장 평균이 작을 수도 있으므로, 같이 비교해 주어야 함
   3. slice가 4이상일 때
     -  4 이상인 부분집합의 평균 들은 위의 2,3인 부분집합의 평균보다 클수 없음   
   
*Referece

https://sooho-kim.tistory.com/45
https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=alwlren_00&logNo=221603639510

"""

# 1. Referecne (100%)
def solution(A):
    # 초기 값
    min_avg = (A[0] + A[1]) / 2
    min_idx = 0
        
    for i in range(2, len(A)):
        # slice가 3일 때
        avg = (A[i-2] + A[i-1] + A[i])/3
        if min_avg > avg:
            min_avg = avg
            min_idx = i - 2  # starting point
        
        # slice가 2일 때
        avg = (A[i-1] + A[i])/2
        if min_avg > avg:
            min_avg = avg
            min_idx = i - 1 # starting point

    return min_idx


# 2. 내 답 (Performance 0%)- O(N**2)
def solution(A):
    N=len(A)
    save_ls = [0]*N
    prefix_sum=0
    for i,v in enumerate(A):
        prefix_sum+=v
        save_ls[i]=prefix_sum

    min_value = 100000
    answer = 0
    for i in range(N):
        for j in range(i+1,N):
            avg_value = (save_ls[j]-save_ls[i]+A[i])/(j-i+1)         
            if avg_value < min_value:
                min_value=avg_value
                answer=i
            
    return answer