#n<=10
n=int(input())
#데이터와 그래프 입력
data=[]
for i in range(n):
    data.append(list(input()))
graph=[]
for i in range(n):
    graph.append(list(input()))

#시계방향
dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]
mine=False
for x in range(n):
    for y in range(n):
        if graph[x][y]=='x':
            if data[x][y]=='*':
                mine=True
            cnt=0
            for i in range(8):
                nx=x+dx[i]
                ny=y+dy[i]
                if nx<0 or nx>=n or ny<0 or ny>=n: continue
                if data[nx][ny]=='*':
                    cnt+=1
            graph[x][y]=cnt
        else: continue
if mine==True:
    for i in range(n):
        for j in range(n):
            if data[i][j]=='*':
                graph[i][j]='*'

for i in graph:
    for j in i:
        print(j, end='')
    print()

