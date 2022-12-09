"""
20221210

- 여행경로
- type: DFS/BFS
- Problem : 
    https://school.programmers.co.kr/learn/courses/30/lessons/43164
    
주의할점
  - 실패) visited 단위가 Country면 안됨.. 그러면 cur -> next 갱신할때 꼬여버림
  - Queue에서 나올때마다 check해야하는 것
    - 현재까지 온 경로
    - 사용된 티켓 여부
  - 리스트 내 리스트(문자열) 있어도, 통으로 sort하면 내부 원소에 따라 정렬됨! 
  Reference 참고
  1. BFS
    - (현재 공항, 경로, 사용한 티켓) 순으로 Queue에 저장 (BFS 활용 + tracking 할때는 이런식으로!!)
    - Queue 추가 조건 : (현재 공항에서 갈수 있는 티켓) & (사용되지 않은 티켓)
      - 만족할 경우 : (다음 공항, 경로 추가, 사용한 티켓 추가)
    - 종료 조건 : 사용한 티켓 수 == 전체 티켓 수
  2. DFS + 백트래킹
    - BFS와 동일한 매커니즘
    - visited를 Ticket으로 해주면 됨
    - 백트래킹 
       - visited을 다시 False로 풀어주지 않으면, 한 경로만 해보고 끝남
       - 여러 경로가 있을 수 있기때문에 다시 재귀적으로 거슬러 올라가면서 티켓을 살려줘야함
    - dfs함수를 solution 내에 정의하면 answer같은 변수를 global 정의 안해도 됨

*백트래킹 (양궁대회 문제)
 - 한번만 방문처리하면 끝나는 문제가 아니라, 모든 경우의 수를 돌아봐야하는 경우 사용해야함
 - 이 경우 DFS는 백트래킹
 - BFS는 이전에 왔던 경로 (티켓 사용여부 등)을 queue에 같이 넣어주어야한다.

*Referece
https://lottegiantsv3.tistory.com/27
"""

# 정렬 확인
a = ["ICN", "SFO", "ATL", "ICN", "ATL", "SFO"]
b = ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
check = [a,b]
print(sorted(check))


# 1. Reference (BFS)
from collections import deque
def solution(tickets):
    answer = []
    q = deque()
    q.append(("ICN",["ICN"], []))
    
    while q:
        airport, path, used = q.popleft()

        if len(used) == len(tickets):
            answer.append(path)
        
        for idx, ticket in enumerate(tickets):
            if ticket[0] == airport and not idx in used:
                q.append((ticket[1], path+[ticket[1]], used+[idx]))
                
    answer.sort()
    return answer[0]

# 2. Reference (DFS + 백트래킹)
def solution(tickets):
    answer = []
    
    visited = [False]*len(tickets)
    
    def dfs(airport, path):
        print(path)
        if len(path) == len(tickets)+1:
            answer.append(path)
            return
        
        for idx, ticket in enumerate(tickets):
            if airport == ticket[0] and visited[idx] == False:
                visited[idx] = True
                dfs(ticket[1], path+[ticket[1]])
                visited[idx] = False
        
    dfs("ICN", ["ICN"])
    
    answer.sort()
    return answer[0]
print()
solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])

# 3. 내 답 (실패 ㅠㅠ)
from collections import deque
def get_graph(tickets):
    ls_ = set([j for i in tickets for j in i])
    graph = {c:[] for c in ls_}
    visited = {t:[] for t in ls_}
    for a,b in tickets:
        graph[a].append(b)
    return graph, visited, len(ls_)

def isvalid_ticket(ls,ne_t):
    for i in range(len(ls)-2):
        if ls[i]==ls[-1]:
            if ls[i+1]==ne_t:
                return False
    return True      
        
def solution(tickets):
    graph, visited, n = get_graph(tickets)
    start="ICN"
    q = deque()
    q.append(start)
    visited[start]+=[start]
    while q:
        cur_t = q.popleft()
        for next_t in graph[cur_t]:
            
            if isvalid_ticket(visited[cur_t], next_t):
                q.append(next_t)
                visited[next_t] = visited[cur_t] + [next_t]
    answer = []
    for v in visited.values():
        if len(v)==n:
            answer.append(v)
    return answer
