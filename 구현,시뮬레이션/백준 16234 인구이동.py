#  (1 ≤ N ≤ 50, 1 ≤ L ≤ R ≤ 100)
from collections import deque
def bfs(q,visited,stack):
    while q:
        x,y=q.popleft()
        # print(x,y)
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n: continue
            if visited[nx][ny]==True: continue
            if abs(graph[nx][ny]-graph[x][y])>=L and abs(graph[nx][ny]-graph[x][y])<=R:
                visited[nx][ny]=True
                q.append((nx,ny))
                stack.append([nx,ny])
    return stack
n,L,R=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))    

dx=[0,0,1,-1]
dy=[1,-1,0,0]
ans=0
while True:
    visited=[[False]*n for i in range(n)]
    isTrue=False
    for i in range(n):
        for j in range(n):
            if visited[i][j]==True: continue
            visited[i][j]=True
            q=deque()
            q.append((i,j))
            stack=[[i,j]]
            tmp=bfs(q,visited,stack)
            total=0
            if len(tmp)>1:
                isTrue=True
                for a,b in stack:
                    total+=graph[a][b]
                total=total//len(stack)
                for a,b in stack:
                    graph[a][b]=total
    if isTrue==False:
        break
    else:
        ans+=1
print(ans)
