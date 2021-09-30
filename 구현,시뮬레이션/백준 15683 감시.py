from collections import deque
def dfs(graph,cur,CCTV,visited):
    global ans
    if cur==cnt:
        tmp=0
        for i in range(n):
            for j in range(m):
                if graph[i][j]==0 and not visited[i][j]:
                    tmp+=1
        if tmp<ans:
            ans=tmp
        return
    #현재 CCTV의 x,y와 종류
    x,y,tv=CCTV[cur][0],CCTV[cur][1],CCTV[cur][2]
    #4방향 회전
    for i in range(4):
        new_dir=[]
        if tv==1:
            new_dir.append(i)
        elif tv==2:
            new_dir.append(i)
            new_dir.append((i+2)%4)
        elif tv==3:
            new_dir.append(i)
            new_dir.append((i+1)%4)
        elif tv==4:
            new_dir.append(i)
            new_dir.append((i+1)%4)
            new_dir.append((i+3)%4)
        q=deque()
        for _ in new_dir:
            nx=x+dx[_]
            ny=y+dy[_]
            while 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny]==6:
                    break
                if visited[nx][ny]==False and graph[nx][ny]==0:
                    visited[nx][ny]=True
                    graph[nx][ny]='#'
                    q.append([nx,ny])
                nx+=dx[_]
                ny+=dy[_]

        dfs(graph,cur+1,CCTV,visited)
        while q:
            nx,ny=q.popleft()
            visited[nx][ny]=False
            graph[nx][ny]=0

n,m=map(int,input().split())
graph=[]
CCTV=[]
CCTV5=[]
cnt=0
visited=[[False]*m for i in range(n)]
for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(m):
        if 0<graph[i][j]<5:
            CCTV.append([i,j,graph[i][j]])
            cnt+=1
            visited[i][j]=True
        elif graph[i][j]==5:
            CCTV5.append([i,j])
#북,동,남,서
dx=[-1,0,1,0]
dy=[0,1,0,-1]
#CCTV5처리
if len(CCTV5)>0:
    for x,y in CCTV5:
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            while 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==6: break
                if graph[nx][ny]==0: 
                    graph[nx][ny]='#'
                nx+=dx[i]
                ny+=dy[i]
ans=2147000000
# for i in range(n):
#     for j in range(m):
#         print('%2s'%graph[i][j], end=' ')
#     print()
dfs(graph, 0,CCTV,visited)
print(ans)
