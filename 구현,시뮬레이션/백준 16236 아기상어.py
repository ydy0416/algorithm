from collections import deque
def bfs(q):
    global ans
    visited=[[False]*n for i in range(n)]
    can_eat=[]
    while q:
        # print(q)
        for _ in range(len(q)):  # **현재 큐 갯수만큼만 진행**
            x,y,size,cnt,dis=q.popleft()
            for i in range(4): #네방향 탐색
                nx=x+dx[i]
                ny=y+dy[i]
                #범위이탈 or 상어크기보다 크면 무시
                if nx<0 or nx>=n or ny<0 or ny>=n: continue
                if not visited[nx][ny]:
                    # print('nx,ny:',nx,ny)
                    visited[nx][ny]=True
                    if graph[nx][ny]>size: continue
                    if 0<graph[nx][ny]<=size:
                        #사이즈가 같을경우 지나가기만
                        if graph[nx][ny]==size:
                            q.append((nx,ny,size,cnt,dis+1))
                        #사이즈가 나보다 작을경우 먹기
                        elif 0<graph[nx][ny]<size:
                            can_eat.append([nx,ny])
                    elif graph[nx][ny]==0:
                        q.append((nx,ny,size,cnt,dis+1))

        if can_eat:
            nx,ny=min(can_eat)
            # print('nx,ny',nx,ny)
            #방문기록 ,큐 초기화
            visited=[[False]*n for k in range(n)]
            graph[nx][ny]=0
            q=deque()
            cnt+=1 #먹은횟수
            ans=dis+1
            # print('먹은곳:%s,%s 거리: %s size: %s '%(nx,ny, ans,size))
            if cnt==size:
                q.append((nx,ny,size+1,0,dis+1))
            else:
                q.append((nx,ny,size,cnt,dis+1))
            can_eat=[]

n=int(input())
graph=[]
q=deque()
for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(n):
        if graph[i][j]==9:
            q.append((i,j,2,0,0)) #인덱스, 초기사이즈,먹은횟수,이동거리
            graph[i][j]=0

ans=0
dx=[-1,0,0,1]
dy=[0,-1,1,0]

bfs(q)
print(ans)