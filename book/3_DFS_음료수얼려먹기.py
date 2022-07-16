"""
 - 음료수 얼려 먹기
 - type : DFS

*DFS는 하나의 노드에서 계속 타고 들어간다는 것(재귀) 기억
*방문처리는 그냥 graph에 처리하면 간편

"""

N,M = map(int,input().split())
graph=[]
for i in range(N):
    graph.append(list(map(int,input().split())))

def ice_dfs(x,y):
    if (x < 0) | (x >= N) | (y < 0) | (y >= M):
        return False
    if graph[x][y]==0:
        graph[x][y]=1
        ice_dfs(x-1,y)
        ice_dfs(x+1,y)
        ice_dfs(x,y-1)
        ice_dfs(x,y+1)
        return True
    return False

result=0
for i in range(N):
    for j in range(M):
        if ice_dfs(i,j):
            print(i,j)
            result+=1
print(result)    
    

