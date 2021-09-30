#  N(2 ≤ N ≤ 500,000)
import sys
sys.setrecursionlimit(10**5)
def dfs(node,depth):
    global cnt
    num=graph[node][0]
    if len(graph[node])==1 and visited[num]==True:
        cnt+=depth
        return
    for i in graph[node]:
        if visited[i]==True:continue
        visited[i]=True
        dfs(i,depth+1)

n=int(input())
graph=[[] for i in range(n+1)]
for i in range(n-1):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
cnt=0
visited=[False]*(n+1)
visited[1]=True
dfs(1,0)
if cnt%2==0:
    print('No')
else:
    print('Yes')