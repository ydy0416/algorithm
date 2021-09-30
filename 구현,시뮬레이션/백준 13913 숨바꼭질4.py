from collections import deque

def bfs():
    q=deque()
    q.append(n)
    while q:
        v=q.popleft()
        if v==k:
            print(dist[v])
            ans=[]
            while v!=n:
                ans.append(v)
                v=path[v]
            ans.append(n)
            ans.reverse()
            print(' '.join(map(str,ans)))
            # print('path:',path)
            return

        for next_step in (v-1,v+1,v*2):
            if 0<=next_step<100001 and not dist[next_step]:
                dist[next_step]=dist[v]+1
                q.append(next_step)
                path[next_step]=v
        

n,k=map(int,input().split())
dist=[0]*(100001)
path=[0]*(100001)
dy=[1,-1,2]
bfs()