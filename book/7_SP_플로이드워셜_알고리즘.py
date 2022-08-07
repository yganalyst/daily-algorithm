"""
 - 플로이드 워셜 알고리즘

*모든노드에서 모든노드로 가는 최단 경로 계산
*따라서 NxN(노드 수) 최단 경로 매트릭스를 저장
*1개 노드를 제외한 N-1개 노드의 쌍별로, 1개노드를 거쳐갈 경우에 대해 갱신
    D(ab) = min(D(ab), D(ak)+D(kb))
*다이나믹 프로그래밍 방식임
    1. OD 매트릭스 생성 (연결되지 않은 간선은 무한)
    2. 1번 노드부터 거쳐가는 경우를 고려해서 갱신
    3. 마지막 노드까지 2번 과정을 반복 (노드의 개수만큼 갱신해야함)
"""

INF = int(1e9)

n=int(input())
m=int(input())
# 2차원 매트릭스 및 무한값으로 초기화
graph=[[INF]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b]=0

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a][b]=c

# 알고리즘 수행 3중 for문 (겨처갈노드, 출발노드, 도착노드)
# 거쳐갈 노드와 이를 제와한 노드들을 고려하진 않음 (어짜피 최소라 갱신안됨)
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b], graph[a][k]+graph[k][b])
            
for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b]==INF:
            print("INFINITY", end=' ')
        else:
            print(graph[a][b], end=' ')
    print()