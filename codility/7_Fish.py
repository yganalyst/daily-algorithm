"""
20221217

- Fish
- type: Stacks and Queues
- level: Easy
- Problem : 
    https://app.codility.com/programmers/lessons/7-stacks_and_queues/fish/

*주의할점
   1. 내 답
   - Down stream 물고기를 stack에 저장
   - up stream이 나타날때마다 stack과 하나하나 비교하도록 구성
   - 살아남으면 list에 추가하는 방식
   2. Reference (재귀)
   - stack을 while문 대신 재귀함수를 만들어 활용

*Referece
https://smecsm.tistory.com/223

"""
# 1. 내 답 (100%) - O(N)
def solution(A, B):

    N = len(A)
    up_fish = []
    down_fish = []
    for i in range(N):
        # Downstream 물고기
        if B[i]==1:
            down_fish.append(A[i])
        # Upstream 물고기
        else:
            # down이 없는 경우 - 올라가세요~
            if not down_fish:
                up_fish.append(A[i])

            # down이 있는 경우 - 싸워야해
            else:
                while down_fish:
                    k = down_fish.pop()
                    if k < A[i]:
                        continue
                    else:
                        down_fish.append(k)
                        break
                # 끝까지 살아남았으면 추가
                if not down_fish:
                    up_fish.append(A[i])

    return len(up_fish+down_fish)

# 2. Reference (재귀 이용)
def solution(A, B):
    
    # 최종 물고기 수를 위한 배열
    fishes = []
    
    # 재귀 함수
    def stack_check():
        p = fishes.pop()
        if p[1] == 1 and ab[1] == 0:
            if p[0] > ab[0] :
                fishes.append(p)
            else :
                if fishes:
                    # fishes에 담겨있는 물고기를 계속 잡아먹을 수 있기 때문에 재귀함수로 호출
                    stack_check()
                else :
                    fishes.append(ab)
                
        else :
            fishes.append(p)
            fishes.append(ab)
	
    # A와 B를 합친 배열 for문
    for ab in zip(A,B):

        if not fishes:
            fishes.append(ab)
            continue

        stack_check()
        
    return len(fishes)
