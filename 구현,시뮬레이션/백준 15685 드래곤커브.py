dx=[0,-1,0,1]
dy=[1,0,-1,0]
n=int(input())
graph=[[0]*101 for i in range(101)]
for _ in range(n):
    y,x,d,g=map(int,input().split())
    tmp=[d]
    q=[d]
    graph[x][y]=1
    for _ in range(g+1):
        for i in q:
            x=x+dx[i]
            y=y+dy[i]
            graph[x][y]=1
        q=[(k+1)%4 for k in tmp]
        q.reverse()
        tmp=tmp+q
#     for i in graph:
#          print(i)
#     print()
cnt=0
for i in range(100):
    for j in range(100):
        if graph[i][j]==1 and graph[i][j+1]==1 and graph[i+1][j]==1 and graph[i+1][j+1]==1:
            cnt+=1
print(cnt)
    
