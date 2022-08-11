"""
 - 다익스트라 알고리즘

특정 노드에서 다른 모든 노드들까지의 최단 경로 계산

1. 출발노드를 설정한다.
2. 최단 거리 테이블을 초기화 한다.
3. 방문하지 않은 노드 중에서 최단거리가 가장 짧은 노드를 선택한다.
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
5. 3,4 과정을 반복한다.

*경로도 출력하고 싶으면, 현재 노드의 이전 노드(부모노드)가 어떤건지 기록해놓으면 됨
"""

n,m=map(int,input().split())
start = int(input())
graph = [[] for _ in range(n+1)]

visited=[False]*(n+1)
distance=[int(1e9)]*(n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def get_smallest_node():
    min_value=int(1e9)
    index=0
    for i in range(1,n+1):
        if distance[i]<min_value and not visited[i]:
            min_value = distance[i]
            index=i
    return index

def dijkstra(start):
    # 출발 기록
    distance[start]=0
    visited[start]=True
    for j in graph[start]:
        distance[j[0]]=j[1]
        
    # start 제외한 노드 수 만큼 반복
    for i in range(n-1):
        # 최단 거리 노드 추출
        now=get_smallest_node()
        # 방문처리
        visited[now]=True
        
        for j in graph[now]:
            # 현재 노드에서 갈 수 있는 다른 노드 cost 계산
            cost = distance[now]+j[1]
            # 기존 것 보다 더 짧은 경우 갱신
            if cost < distance[j[0]]:
                distance[j[0]]=cost
    
dijkstra(start)
                
for i in range(1,n+1):
    if distance[i]==int(1e9):
        print("INFINITY")
    else:
        print(distance[i])
        
        
        
        