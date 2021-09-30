import sys
sys.setrecursionlimit(10**9)
# 1. 자식노드로 향하는 단방향그래프 작성
# 2. 제거해야할 노드를 미리 방문처리
# 3. 리프노드인지 검사(자식노드x && 지우고싶은 노드아님) or (자식노드가 있지만 자식노드가 지우고 싶은 노드일 때)
def dfs(node):
    global ans
    #리프노드
    if len(graph[node])==1:
        tmp=graph[node][0]
    if (len(graph[node])==0 and visited[node]==False) or (len(graph[node])==1 and visited[tmp]==True): #리프노드인지 판단
        ans+=1
        return 
    for i in graph[node]:
        if visited[i]==True: continue
        dfs(i)

n=int(input())
data=list(map(int,input().split()))
target=int(input())
graph=[[] for i in range(n)]
for i in range(len(data)):
    num=data[i]
    if num==-1: 
        root=i
        continue
    graph[num].append(i)

visited=[False]*(n)
visited[target]=True #미리 방문처리함으로써 타겟의 서브트리 방문x

ans=0
if target==root:   
    print(0)
else:
    dfs(root)
    print(ans)
