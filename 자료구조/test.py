from collections import deque
n,m,t=map(int,input().split())
graph=[]
air=[]
q=deque()
for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(m):
        if graph[i][j]==-1:
            air.append(i)
        elif graph[i][j]>0:
            q.append((i,j,graph[i][j],0))
for j in graph:
    print(j)
dx=[0,0,1,-1]
dy=[1,-1,0,0]
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
        if y==7:
            print('x,y,data,tmp_q:',x,y,data,tmp_q)
        if x<0 or x>=n or y<0 or y>=m:
            x-=dx[dir]
            y-=dy[dir]
            tmp_q.append(data)
            break
        tmp_q.append(graph[x][y])
        graph[x][y]=data
print()
for j in graph:
    print(j)