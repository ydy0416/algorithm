import sys
def dfs(a,graph,visited,cnt,line):
    global ans
    if cnt>3:
        return
    #사다리가 똑바로 내려오는지 시뮬레이션
    for i in range(1,n+1):
        x,y=1,i
        isTrue=True
        while True:
            if x<1 or x>h or y<1 or y>n: break
            if graph[x][y]>0:
                #왼쪽으로 이동
                if graph[x][y-1]==graph[x][y]:
                    y=y-1
                #오른쪽으로 이동
                elif graph[x][y+1]==graph[x][y]:
                    y=y+1
            #다음행탐색
            x+=1
        #열의 시작과 끝이 다르게되면 break
        if i!=y:
            isTrue=False
            break
    #모든 열의 시작과 끝이 같음, 최솟값 갱신
    if isTrue==True:
        ans=min(ans,cnt)

    #그래프 출력
    # for i in graph:   
    #     print(i)
    # print()

    #가로줄 긋기
    for i in range(a,h+1):
        for j in range(1,n):
            if graph[i][j]==0 and graph[i][j+1]==0: 
                if visited[i][j]==True and visited[i][j+1]==True:
                    continue
                graph[i][j],graph[i][j+1]=line, line
                visited[i][j],visited[i][j+1]=True,True
                dfs(i,graph,visited,cnt+1,line+1)
                graph[i][j],graph[i][j+1]=0,0
                visited[i][j],visited[i][j+1]=False,False

n,m,h=map(int,input().split())
graph=[[0]*(n+1) for i in range(h+1)]
ans=2147000000
line=1
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a][b]=line
    graph[a][b+1]=line
    line+=1

visited=[[False]*(n+1) for i in range(h+1)]
dfs(1,graph,visited,0,line)
            
if ans==2147000000:
    print(-1)
else:       
    print(ans)
    