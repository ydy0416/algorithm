from collections import deque
def dfs(graph,cur,CCTV,check):
    global ans
    if cur==cnt:
        print('cur')
        tmp=0
        for i in range(n):
            for j in range(m):
                if graph[i][j]==0 and not check[i][j]:
                    tmp+=1
        print('tmp:', tmp)
        if tmp<ans:
            ans=tmp
        return
    #4방향 회전
    x,y,tv=CCTV[cur][0],CCTV[cur][1],CCTV[cur][2]
    print('x,y,tv:',x,y,tv)
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
        print('new_dir:', new_dir)
        for _ in new_dir:
            nx=x+dx[_]
            ny=y+dy[_]
            while 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny]==6:
                    break
                if check[nx][ny]==False:
                    check[nx][ny]=True
                    q.append([nx,ny])
                nx+=dx[_]
                ny+=dx[_]

        dfs(graph,cur+1,CCTV,check)
        print('q:',q)
        while q:
            nx,ny=q.popleft()
            if not graph[nx][ny]:
                check[nx][ny]=False

n,m=map(int,input().split())
graph=[]
CCTV=[]
CCTV5=[]
cnt=0
check=[[False]*m for i in range(n)]
for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(m):
        if 0<graph[i][j]<5:
            CCTV.append([i,j,graph[i][j]])
            cnt+=1
            check[i][j]=True
        elif graph[i][j]==5:
            CCTV5.append([i,j])
#시계방향
dx=[-1,0,1,0]
dy=[0,1,0,-1]
#CCTV5처리
if len(CCTV5)>0:
    for x,y in CCTV5:
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            while True:
                if nx<0 or nx>=n or ny<0 or ny>=m:
                    break
                graph[nx][ny]='#'
                nx+=dx[i]
                ny+=dy[i]
ans=2147000000
dfs(graph, 0,CCTV,check)
print(ans)
