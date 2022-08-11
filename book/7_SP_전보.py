"""
 - 전보
 - type : 최단 경로
 - problem :
     N개의 도시가 있고, 한 도시에서 다른 도시로 메세지를 보낼때는 연결되어 있어야함
     도시 C에서 메세지를 보내서 받게되는 도시의 총 개수와 걸리는 시간 계산하기
    
*특정 노드에서 다른 모든 노드간의 최단경로를 계산하는 문제로 다익스트라가 적합
*플로이드 워셜 사용해도 되지만, N과 M의 범위가 매우 크기때문에 효육적인 다익스트라 사용
*총 걸리는 시간은 제일 멀리있는 노드만 알면 된다!!
*heapq는 앞의 원소를 기준으로 최소 힙 이용함
"""

import heapq
INF=int(1e9)

n,m,start=map(int,input().split())    
graph=[[] for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    x,y,z=map(int,input().split())    
    graph[x].append((y,z))


def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost, i[0]))
        
dijkstra(start)

cnt=0
max_distance=0
for d in distance:
    if d!= INF:
        # 도달할 수 있는 경우 카운트
        cnt+=1
        # 가장 멀리 있는 노드만 살리기
        max_distance = max(max_distance, d)
# 시작노드는 제외해야하므로 -1
print(cnt-1, max_distance)
