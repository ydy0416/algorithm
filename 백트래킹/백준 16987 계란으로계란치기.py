def dfs(start,visited,cur,cnt):
    global ans
    if data[start][0]<0:
        cnt+=1
        while True:
            start+=1
            if start==n-1:
                break
            if data[start][0]>0:
                break
    #최근에 든 계란이 마지막일경우
    if start==n-1:
        if cnt>ans:
            ans=cnt
         
    for i in range(n):
        if visited[i]==True or data[i][0]<0: continue
        visited[i]=True
        data[start][0]-=data[i][1]
        data[i][0]-=data[start][1]
        if data[i][0]<0:
            cnt+=1
        dfs(start,visited,cur+1,cnt)
        visited[i]=False
        data[start][0]+=data[i][1]
        data[i][0]+=data[start][1]

#1<=n<=8
n=int(input())
data=[]

#내구도, 무게
for i in range(n):
    data.append(list(map(int,input().split())))

ans=0
for start in range(n):
    visited=[False]*n
    visited[start]=True
    dfs(start,visited,0,0)