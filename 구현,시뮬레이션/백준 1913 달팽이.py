n=int(input())
m=int(input())
dir=[[0]*n for i in range(n)]
start=n*n
dx=[1,0,-1,0]
dy=[0,1,0,-1]

x,y=0,0
i=3
dir[x][y]=n*n
start=n*n-1
while True:
    #중간지점 도착시 break
    if x==((n+1)//2)-1 and y==((n+1)//2)-1: break
    if i==3:
        i=0
    elif i==0:
        i=1
    elif i==1:
        i=2
    elif i==2:
        i=3
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
        dir[x][y]=start
        start-=1
for i in range(n):
    for j in range(n):
        if dir[i][j]==m:
            ans=[i+1,j+1]
        print(dir[i][j], end=' ')
    print()
print(ans[0], ans[1])