
# 4 ≤ N, M ≤ 500
n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))
# 모든경우의 수
# graph[i][j]+graph[i][j+1]+graph[i][j+2]+graph[i][j+3]
# graph[i][j]+graph[i+1][j]+graph[i+2][j]+graph[i+3][j]
# graph[i][j]+graph[i][j+1]+graph[i+1][j]+graph[i+1][j+1]
# graph[i][j]+graph[i+1][j]+graph[i+1][j+1]+graph[i+1][j+2]
# graph[i][j]+graph[i+1][j]+graph[i+2][j]+graph[i+2][j+1]
# graph[i][j]+graph[i][j+1]+graph[i][j+2]+graph[i-1][j+2]
# graph[i][j]+graph[i][j+1]+graph[i+1][j+1]+graph[i+1][j+2]
# graph[i][j]+graph[i][j+1]+graph[i][j+2]+graph[i+1][j]
# graph[i][j]+graph[i][j+1]+graph[i][j+2]+graph[i+1][j+1]
# graph[i][j]+graph[i][j+1]+graph[i-1][j+1]+graph[i-1][j+2]
# graph[i][j]+graph[i+1][j]+graph[i+2][j]+graph[i+1][j+1]
# graph[i][j]+graph[i][j+1]+graph[i-1][j+1]+graph[i+1][j+1]
# graph[i][j]+graph[i][j+1]+graph[i-1][j+1]+graph[i][j+2]

# graph[i][j]+graph[i][j+1]+graph[i-1][j+1]+graph[i-2][j+1]
# graph[i][j]+graph[i][j+1]+graph[i][j+2]+graph[i+1][j+2]
# graph[i][j]+graph[i+1][j]+graph[i+2][j]+graph[i][j+1]
# graph[i][j]+graph[i+1][j]+graph[i+1][j+1]+graph[i+1][j+2]
# graph[i][j]+graph[i][j+1]+graph[i-1][j+1]+graph[i+1][j]
# graph[i][j]+graph[i][j+1]+graph[i+1][j+1]+graph[i+1][j+2]
dx=[[0,0,0,0],[0,1,2,3],[0,0,1,1],[0,1,1,1],[0,1,2,2],[0,0,0,-1],[0,0,1,1],[0,0,0,1],[0,0,0,1],[0,0,-1,-1],[0,1,2,1],[0,0,-1,1],[0,0,-1,0],[0,0,-1,-2],[0,0,0,1],[0,1,2,0],[0,1,1,1],[0,0,-1,1],[0,0,1,1],[0,0,1,2],[0,1,1,2]]
dy=[[0,1,2,3],[0,0,0,0],[0,1,0,1],[0,0,1,2],[0,0,0,1],[0,1,2,2],[0,1,1,2],[0,1,2,0],[0,1,2,1],[0,1,1,2],[0,0,0,1],[0,1,1,1],[0,1,1,2],[0,1,1,1],[0,1,2,2],[0,0,0,1],[0,0,1,2],[0,1,1,0],[0,1,1,2],[0,1,1,1],[0,0,1,1]]
ans=0
for x in range(n):
    for y in range(m):
        for k in range(21):
            tmp=0
            for j in range(4):
                nx=x+dx[k][j]
                ny=y+dy[k][j]
                if nx<0 or nx>=n or ny<0 or ny>=m:
                    break
                tmp+=graph[nx][ny]
                if tmp>ans:
                    ans=tmp
print(ans)


