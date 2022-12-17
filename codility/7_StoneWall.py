"""
20221217

- StoneWall
- type: Stacks and Queues
- level: Easy
- Problem : 
    https://app.codility.com/programmers/lessons/7-stacks_and_queues/stone_wall/

*주의할점
   1. 내 답
    - 아이디어는 맞았으나, performance가 44%가 나옴 ㅠㅠ 
    - 기준 블록을 유지 또는 갱신시키면서, 각 index마다 채워주고 남은 공간을 다시 stack에 넣어주는 형태
    - 새블록을 놓아야 하는 경우 = 높이가 낮아지거나, 다시 한바퀴 돌아온 경우, 띄어져 있는 경우
       - (현재 인덱스 - 기준 인덱스)!=1 일때임, 결국 연속되고 있냐만 보면 되는 것
       
   2. Reference
    - 아이디어는 유사한데, 그냥 해당 index 칸에서 기준을 그때그때만들어 count함
    - 그리고 내 코드는 밑에서부터 차근차근 쌓아올리는 형태라면,
    - reference는 높이 변화를 체크하면서 위에서 부터 타고 내려오는 형태임
    - 2번째 블로그 친절한 그림 참고
    

*Referece
https://smecsm.tistory.com/225
https://velog.io/@jonas-jun/Codility-Wall

"""
# 1. Reference (100%)
H=[8, 8, 5, 7, 9, 8, 7, 4, 8]
def solution(H):
    
    stack = []
    count = 0

    for h in H:
        # 현재 블록(h)이 이전 블록(stack[-1])보다 작으면,
        # 즉, 높이가 감소하면,
        # 작기 전까지 stack에서 빼기
        while stack and stack[-1] > h:
            stack.pop()
            
        # 현재 블록(h)이 이전 블록(stack[-1])보다 크면,
        # 즉, 높이가 증가하면,
        # 새로운 블록 추가
        if not stack or stack[-1] < h:
            count += 1
            stack.append(h)
        
    return count

# 2. 내 답 (Performance 44%)
def solution(H):
    # [8,8,5,7,9,8,7,4,8]
    H_idx = list(enumerate(H))
    stand_idx, stand_h = H_idx.pop(0)
    result = 1
    while H_idx:
        cur_idx, cur_h = H_idx.pop(0)

        if cur_h < stand_h or ((cur_idx - stand_idx) != 1):
            stand_h = cur_h
            result +=1
        else:
            diff_h = cur_h-stand_h
            if diff_h:
                H_idx.append((cur_idx,diff_h))
        stand_idx = cur_idx

    return result 


