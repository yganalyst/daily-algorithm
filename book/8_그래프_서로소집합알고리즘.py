"""
 - 서로소 집합 알고리즘

*서로소 집합이란? 공통 원소가 없는 두 집합
*ex) {1,2}, {3,4} 는 공통원소가 없음
*union(하나의 집합으로 합치기), find(특정한 원소가 속한 집합 찾기)

*결국 노드와 간선이 주어졌을때, 루트(최상단)노드가 같은 집합이 몇개냐를 묻는 것임
*(sub graph의 개수)
*경로압축기법 : 루트노드가 바로 부모노드가 됨(검색 복잡도를 줄일 수 있음)
"""

def find_parent(parent, x):
    if parent[x]!=x:
        #return find_parent(parent, parent[x]) # 기존방식
        parent[x]=find_parent(parent, parent[x]) # 경로 압축 기법
    #return x  # 기존 방식
    return parent[x]  # 경로 압축 기법

def union_parent(parent, a, b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
    
v,e=6,4
parent=[0]*(v+1)

for i in range(1,v+1):
    parent[i]=i
    
for i in range(e):
    a,b=map(int,input().split())
    union_parent(parent, a, b)
    
print("각 원소가 속한 집합: ", end='')
for i in range(1,v+1):
    print(find_parent(parent, i), end=' ')
    
print()

print('부모 테이블: ', end=' ')
for i in range(1,v+1):
    print(parent[i], end=' ')