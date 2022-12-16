"""
20221216

- MissingInteger
- type: Prefix Sums
- level: Medium
- Problem : 
    https://app.codility.com/programmers/lessons/5-prefix_sums/genomic_range_query/

*주의할점
   - prefix sum 알고리즘을 구현할 줄 알아야지만 풀 수 있는 문제
   - N개 원소에서 M개의 구간합을 계산할 떄 기존 방법들은 O(N*M)이 소요되는데,
   - 미리 loop 한번 게산 해놓고 다음 Loop에서 답을 내서, O(N+M)으로 줄이는 알고리즘임
   Reference의 prefix sum 설명
   - 문자열 간 최소값 계산을, 어떻게 prefix sum 방식으로 바꿀지가 관건
   - CAGCCTA   (ACGT)
   - [[0,1,0,0]]
     [[0,1,0,0],[1,1,0,0]]
     [[0,1,0,0],[1,1,0,0],[1,1,1,0]]
     [[0,1,0,0],[1,1,0,0],[1,1,1,0],...,[2,3,1,1]]
   - 위와 같이 S[:i] (i=0,N) 에 대한 ACGT를 먼저 Count해서 저장해두고
   - A[Q]와 A[P]를 각 원소 간의 차이를 구하고,
   - 처음으로 0이 아닌 인덱스+1이 결국 minimal impact factor가 됨
   
어렵다..
   
*Referece
https://nachwon.github.io/GenomicRangeQuery/

"""

# 1. Referecne (100%)
def solution(S, P, Q):
    A = [[0, 0, 0, 0]]
    counter = [0] * 4
    result = []
    for i in S:
        if i == "A":
            counter[0] += 1
            A.append(counter[:])
        elif i == "C":
            counter[1] += 1
            A.append(counter[:])
        elif i == "G":
            counter[2] += 1
            A.append(counter[:])
        elif i == "T":
            counter[3] += 1
            A.append(counter[:])
    
    for p,q in zip(P,Q):
        for i in range(4):
            val = A[q+1][i] - A[p][i]
            if val != 0:
                result.append(i + 1)
                break    
    return result



# 2. Reference (50%) - 이것도 실패 (원래는 됐었던 것 같음)
def solution(S, P, Q): 
    if_dict = {"A":1,"C":2,"G":3,"T":4}
    answer = []
    for p,q in zip(P,Q):
        sub_s = S[p:q+1]
        if "A" in sub_s:
            answer.append(if_dict["A"])
        elif "C" in sub_s:
            answer.append(if_dict["C"])
        elif "G" in sub_s:
            answer.append(if_dict["G"])
        else:
            answer.append(if_dict["T"])
    return answer

# 3. 내 답 (Performance 0%)- O(N*M)
def solution(S, P, Q): 
    if_dict = {"A":1,"C":2,"G":3,"T":4}
    answer=[]
    for p,q in zip(P,Q):
        sub_s = S[p:q+1]
        min_if = if_dict[min(sub_s)]
        answer.append(min_if)
    return answer