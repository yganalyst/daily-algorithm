"""
20221208

- 단어 변환
- type: DFS/BFS
- Level: 3
- Problem : 
    https://school.programmers.co.kr/learn/courses/30/lessons/43163
    
주의할점
  - DFS로 잘 풀었으나, 문제조건(단어길이 3~10) 고려를 못함
  - 그리고 바뀔수 있는 단어인지 확인할때, set으로 접근하면 안되고, 철자하나씩 확인해야함 (순서가 있어야 알지)
  - 코드가 좀 길어졌는데, BFS로 푼 reference 참고하자
  
  
** Reference

"""


# 1. 내 답 (DFS)
from collections import deque
def is_near_word(a,b):
    n=len(a)
    check=0
    for i in range(n):
        if a[i]==b[i]:
            check+=1
    if check==n-1:
        return True
    return False

def get_words_graph(begin, words):
    graph = {w:[] for w in [begin]+words}
    for w1 in [begin]+words:
        for w2 in words:
            if w1==w2:
                continue
            if is_near_word(w1,w2):
                graph[w1].append(w2)
    return graph
    
def dfs(cnt, cur_word, target, graph, visited):
    global min_cnt
    if cur_word==target:
        min_cnt = min(min_cnt, cnt)
        return
    
    visited[cur_word]=True
    for next_word in graph[cur_word]:
        if not visited[next_word]:
            dfs(cnt+1, next_word, target, graph, visited)
    
def solution(begin, target, words):
    global min_cnt

    min_cnt = 100
    visited = {w:False for w in words}
    graph = get_words_graph(begin, words)
    dfs(0, begin, target, graph, visited)
    
    if min_cnt == 100:
        answer = 0
    else:
        answer = min_cnt
    return answer


# 2. Reference (BFS)
from collections import deque
def get_adjacent(current, words):
    for word in words:
        if len(current) != len(word):
            continue

        count = 0
        for c, w in zip(current, word):
            if c != w:
                count += 1

        if count == 1:
            yield word


def solution(begin, target, words):
    dist = {begin: 0}
    queue = deque([begin])

    while queue:
        current = queue.popleft()

        for next_word in get_adjacent(current, words):
            if next_word not in dist:
                dist[next_word] = dist[current] + 1
                queue.append(next_word)

    return dist.get(target, 0)