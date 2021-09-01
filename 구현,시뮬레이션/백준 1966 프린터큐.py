from collections import deque
import heapq
T=int(input())
for _ in range(T):
    n,m=map(int,input().split())
    data=list(map(int,input().split()))
    q=deque([data[i],i] for i in range(n))
    data.sort()
    cnt=0
    while q:
        maximum=data[-1]
        # print('maximum, q:',maximum,q)
        if q[0][0]<maximum:
            q.append(q.popleft())
        elif q[0][0]>=maximum:
            cnt+=1
            tmp=q[0]
            if tmp[1]==m:
                break
            else:   
                q.popleft()
                data.pop()

    print(cnt)
