"""
20221202

- 모음사전
- type: 완전탐색
- Level: 2
- Problem : 
    https://school.programmers.co.kr/learn/courses/30/lessons/84512
    
주의할점
  1. 내 답 (DFS 활용)
  - 길이가 1~5자리 까지 단어조합이 사전 순으로 정렬되어야 함
  - 따라서 BFS는 안되고 DFS 재귀 탐색으로 가야됨
  - 재귀탐색이 어짜피 사전순이니, 탐색완료되면 재귀 종료하도록 구현 (모든 단어 탐색보다는 빠름)
     - end와 cnt를 global 변수로 선언
     - counting은 누적해야됨 (파라미터가아니라 내부변수로 선언)
     - 찾을 단어(word)와 맞으면 end에 넣고 종료

**Reference (모든 단어 미리 생성하기)
  2. 그냥 for문 5개로 구현해버리는 방법 (이걸 처음 생각했는데 간단한데 못함)
  3. itertools 라이브러리 product 활용하는 방법

"""

# 1. 내 답 (DFS 활용)
end = 0
cnt = 0
def dfs_search(cur_word,word,spells):
    global end, cnt
    if cur_word==word:
        print(cur_word, word)
        end=cnt
    
    for s in spells:
        if len(cur_word+s)<=5 and not end:
            cnt+=1
            dfs_search(cur_word+s,word,spells)    

def solution(word):
    spells = ["A","E","I","O","U"]
    dfs_search('',word,spells) 
    return end

# 2. Reference (for문으로 조지는 방법)
def solution(word):
    answer = 0
    alpha  = ["A","E","I","O","U",""]
    ans = []
    for i in alpha:
        for j in alpha:
            for k in alpha:
                for l in alpha:
                    for m in alpha:
                        w = i+j+k+l+m
                        if w not in ans: ans.append(w)
    ans.sort()
    answer = ans.index(word)
    return answer

# 3. Reference (product활용)
from itertools import product
def solution(word):
    spells = ["A","E","I","O","U"]
    all_list = []
    for i in range(5):
        for c in product(spells,repeat=i+1):
            all_list.append("".join(c))
    all_list = sorted(all_list)
    return all_list.index(word)+1

