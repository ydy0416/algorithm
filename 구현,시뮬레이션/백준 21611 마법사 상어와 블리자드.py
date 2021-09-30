from collections import deque

#구슬 이동
def move(q):
    x,y=q.popleft()
    while True:
        if x==0 and y==0: break
        nx,ny=x,y
        print('nx,ny:',nx,ny)
        #0이 아닌곳 탐색
        while graph[nx][ny]==0:
            tmpx,tmpy=nx,ny
            nx-=dx[dir[tmpx][tmpy]]
            ny-=dy[dir[tmpx][tmpy]]
        graph[x][y]=graph[nx][ny]
        graph[nx][ny]=0
        x=x-dx[dir[x][y]]
        y=y-dy[dir[x][y]]
        print('graph')
        for i in graph:
            print(i)
        print()

n,m=map(int,input().split())
#그래프
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))

#파괴 방향과 거리
d,s=map(int,input().split())

#방향 그래프
# dir=[[0]*n for i in range(n)]
# dx=[0,-1,1,0,0]
# dy=[0,0,0,-1,1]
# x,y=0,0
# i=1
# while True:
#     if x==((n+1)//2)-1 and y==((n+1)//2)-1: break
#     if i==1:
#         i=4
#     elif i==4:
#         i=2
#     elif i==2:
#         i=3
#     elif i==3:
#         i=1
#     dir[x][y]=i
#     while 0<=x<n and 0<=y<n:
#         x+=dx[i]
#         y+=dy[i]
#         if x<0 or x>=n or y<0 or y>=n: 
#             x-=dx[i]
#             y-=dy[i]
#             break
#         if dir[x][y]!=0:
#             x-=dx[i]
#             y-=dy[i]
#             break
#         dir[x][y]=i
# dir[(n+1)//2-1][(n+1)//2-1]=0

# 방향그래프2  
dir=[[0]*n for i in range(n)]
dx=[0,-1,1,0,0]
dy=[0,0,0,-1,1]
x,y=0,0
i=1
dir[x][y]=4
while True:
    #중간지점 도착시 break
    if x==((n+1)//2)-1 and y==((n+1)//2)-1: break
    if i==1:
        i=4
    elif i==4:
        i=2
    elif i==2:
        i=3
    elif i==3:
        i=1
    while 0<=x<n and 0<=y<n:
        x+=dx[i]
        y+=dy[i]
        if x<0 or x>=n or y<0 or y>=n:
            x-=dx[i]
            y-=dy[i]
            break
        if dir[x][y]!=0:
            x-=dx[i]
            y-=dy[i]
            break
        dir[x][y]=i
dir[(n+1)//2-1][(n+1)//2-1]=0
for i in dir:
    print(i)

#구슬 파괴
x=((n+1)//2)-1
y=((n+1)//2)-1
q=deque()
for i in range(s):
    x+=dx[d]
    y+=dy[d]
    #파괴된구슬 인덱스 저장
    q.append([x,y])
    if x<0 or x>=n or y<0 or y>=n: break    
    graph[x][y]=0
print(q)
#구슬이동
move(q)