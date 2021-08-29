# 2<=n<=10
def dfs(start,arrival,cnt,cost):
    global ans
    if cnt==n-1: 
        if W[arrival][start]==0:
            return
        else:
            cost+=W[arrival][start]
            # print('cost:', cost)
            if ans>cost:
                ans=cost
            return
    
    for i in range(n):
        if visited[i]==True or W[arrival][i]==0: continue
        # print('start,이전 ,이후:', start,arrival, i)
        visited[i]=True
        cost+=W[arrival][i]
        dfs(start,i,cnt+1,cost)
        cost-=W[arrival][i]
        visited[i]=False
    
        

n=int(input())
W=[]
for i in range(n):
    W.append(list(map(int,input().split())))


ans=2147000000
for i in range(n):
    visited=[False]*n
    visited[i]=True
    dfs(i,i,0,0)

print(ans)