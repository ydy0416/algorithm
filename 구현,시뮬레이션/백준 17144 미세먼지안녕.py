from collections import deque
n,m,t=map(int,input().split())
graph=[]
air=[]
q=deque()
time=0
for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(m):
        if graph[i][j]==-1:
            air.append(i)
        elif graph[i][j]>0:
            q.append((i,j,graph[i][j],time))

dx=[0,0,1,-1]
dy=[1,-1,0,0]
breaker=False
while q:
    for _ in range(len(q)): #미세먼지 확산, 현재있는 큐만큼 진행
        x,y,amount,time=q.popleft()
        if time==t:
            breaker=True
            break
        cnt=4
        tmp=deque()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m or graph[nx][ny]==-1:
                cnt-=1
                continue
            tmp.append((nx,ny)) #임시큐에 저장
        while tmp:
            nx,ny=tmp.popleft()
            graph[nx][ny]+=amount//5
            q.append((nx,ny,graph[nx][ny],time+1)) #확산
            # print(nx,ny,graph[nx][ny],time+1)
        dif=graph[x][y]-amount
        graph[x][y]=amount-(amount//5)*cnt+dif
    # print()
    # for j in graph:
    #     print(j)

    if breaker:
        break  
    #공기청정기 위
    x=air[0]
    y=1
    dir=2   #동:0 서:1 남:2 북:3
    tmp_q=deque([graph[x][y]])
    graph[x][y]=0
    for i in range(4):
        if dir==2:  #남쪽이면 동쪽으로 방향바꾸기
            dir=0
        elif dir==0: #동쪽이면 북쪽으로
            dir=3
        elif dir==3: #북쪽이면 서쪽
            dir=1
        elif dir==1: #서쪽이면 남쪽
            dir=2
        while 0<=x<n and 0<=y<m:
            data=tmp_q.popleft()
            x=x+dx[dir]
            y=y+dy[dir]
            if x==air[0] and y==0: break
            if x<0 or x>=n or y<0 or y>=m:
                x-=dx[dir]
                y-=dy[dir]
                tmp_q.append(data)
                break
            tmp_q.append(graph[x][y])
            graph[x][y]=data
    
    #공기청정기 아래
    x=air[1]
    y=1
    dir=3   #동:0 서:1 남:2 북:3
    tmp_q=deque([graph[x][y]])
    graph[x][y]=0
    for i in range(4):
        if dir==3:  #북쪽이면 동쪽으로 방향바꾸기
            dir=0
        elif dir==0: #동쪽이면 남쪽으로
            dir=2
        elif dir==2: #남쪽이면 서쪽
            dir=1
        elif dir==1: #서쪽이면 북쪽
            dir=3
        while 0<=x<n and 0<=y<m:
            data=tmp_q.popleft()
            x=x+dx[dir]
            y=y+dy[dir]
            if x==air[1] and y==0: break
            if x<0 or x>=n or y<0 or y>=m:
                x-=dx[dir]
                y-=dy[dir]
                tmp_q.append(data)
                break
            tmp_q.append(graph[x][y])
            graph[x][y]=data
    time+=1
    q=deque()
    air=[]
    for i in range(n):
        for j in range(m):
            if graph[i][j]==-1:
                air.append(i)
            elif graph[i][j]>0:
                q.append((i,j,graph[i][j],time))

    # print()
    # for j in graph:
    #     print(j)
    # print('_'*50)

ans=0
for i in range(n):
    ans+=sum(graph[i])

print(ans+2)


    