"""
20221208

- 단어 변환
- type: DFS/BFS
- Level: 3
- Problem : 
    https://school.programmers.co.kr/learn/courses/30/lessons/43163
    
주의할점
  1. 내 답 (DFS)
   - DFS로 잘 풀었으나, 문제조건(단어길이 3~10) 고려를 못함
   - 그리고 바뀔수 있는 단어인지 확인할때, set으로 접근하면 안되고, 철자하나씩 확인해야함 (순서가 있어야 알지)
   - 코드가 좀 길어졌는데, BFS로 푼 reference 참고하자
  2. Reference (BFS)
   - get_adjacent 함수에서 zip, yield 활용하여 현재 word에서 바뀔 수 있는 word들을 generator로 반환함
   - dict.get(target,0) 은 target에 해당하는 count , 값이 없으면 0 을 반환
  3. Reference (BFS)
   - 블로그 참고
   - 이것도 결국 최단경로 문제라서 BFS로 푸는 것이 좋음 !!!!! (계속 헷갈리네)
   - BFS는 단계별로 가기때문에, 루프마다 count가 아니라 이전 word에서 몇번째 왔냐만 체크해주면 되는 것임
   - 같은 깊이에서 하나씩 탐색하기때문에 결국 target에 도달하는 그 지점이 최단 경로 길이가 된다..!
** Reference
https://muhly.tistory.com/86
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
        # list(zip("hit",["hot", "dot", "dog", "lot", "log", "cog"]))
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
            print(dist)
            if next_word not in dist:
                dist[next_word] = dist[current] + 1
                queue.append(next_word)

    return dist.get(target, 0)

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
solution(begin,target,words)

# 3. Referecne (BFS 짧음)
from collections import deque
# queue를 위함

def check(s, begin):
    answer = 0
    for i in range(len(s)):
        if list(s)[i] != list(begin)[i]:
            answer += 1
    return True if answer == 1 else False


def solution(begin, target, words):
    if target not in words:
        return 0

    queue = deque()
    queue.append([begin, []])

    while queue:
        n, l = queue.popleft()
        for word in words:
            if word not in l and check(word, n):
                if word == target:
                    return len(l) + 1
                temp = l[0:]
                temp.append(word)
                queue.append([word, temp])

    return 0

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]