"""
 - 미래도시
 - type : 최단 경로
 - problem :
     도시는 N개 노드가 존재하며, 양방향으로 연결되어 있음(cost는 모두 1)
     방문판매원은 1번 노드에 위치하며, K노드를 들려 X노드로 이동해야함
     최단 경로는 ?     

*graph 초기화하는 방법 다시 숙지
    INF로 NxN 매트릭스 생성
    대각선 값은 0으로 대체
    입력값 받기
"""
n,m=5,7
INF=int(1e9)
graph=[[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0

for _ in range(m):
    a,b=map(int,input().split())    
    graph[a][b]=1
    graph[b][a]=1
    
x,k=4,5
for a in range(1,n+1):
    for b in range(1,n+1):
        for c in range(1,n+1):
            graph[b][c] = min(graph[b][c],graph[b][a]+graph[a][c])

result = graph[1][k]+graph[k][x]
if result>=INF:
    print(-1)
else:
    print(result)
    
