import sys
def dfs(x,y,visited,cur,total):
    global ans
    if cur==4:
        # print('ans, total', ans, total)
        if ans<total:
            ans=total
        return 
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if visited[nx][ny]==True:
            continue
        visited[nx][ny]=True
        total+=graph[nx][ny]
        dfs(nx,ny,visited,cur+1,total)
        total-=graph[nx][ny]
        visited[nx][ny]=False

n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append((list(map(int,sys.stdin.readline().split()))))
dx=[0,0,1,-1]
dy=[1,-1,0,0]
ans=0
# 'ㅗ' 모양 전용 
hx=[[0,0,-1,0],[0,1,2,1],[0,0,0,1],[0,0,-1,1]]
hy=[[0,1,1,2],[0,0,0,1],[0,1,2,1],[0,1,1,1]]

for i in range(n):
    for j in range(m):
        visited=[[False]*m for _ in range(n)]
        visited[i][j]=True
        # 'ㅗ'모양 제외 dfs
        dfs(i,j,visited,0,0)
        # 'ㅗ'모양 탐색
        for k in range(4):
            tmp=0
            for h in range(4):
                nx=i+hx[k][h]
                ny=j+hy[k][h]
                if nx<0 or nx>=n or ny<0 or ny>=m:
                    break
                tmp+=graph[nx][ny]
            #     print('nx,ny',nx,ny)
            # print('tmp',tmp)
            if tmp>ans:
                ans=tmp
print(ans)