"""
 - 다익스트라 알고리즘 - 시간복잡도 개선

특정 노드에서 다른 모든 노드들까지의 최단 경로 계산

*O(V^2) -> O(ElogV)  : V 노드 수, E 간선 수
*최단거리가 가장 짧은 노드 찾기(get_smallest_node)가 O(V)였는데 이걸 개선
*힙(heap)자료구조 이용: 우선순위 큐(Priority Queue), 우선순위가 가장 높은 데이터를 먼저 삭제
*heapq 라이브러리 이용
"""

import heapq
# import sys
# input = sys.stdin.readline
INF = int(1e9)

n,m=map(int,input().split())
start = int(input())
graph=[[] for i in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0

    while q:
        # 가장 최단거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 처리된적이 있는 노드라면 pass
        if distance[now]<dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
                
dijkstra(start)

for i in range(1,n+1):
    if distance[i]==INF:
        print("INFINITY")
    else:
        print(distance[i])
