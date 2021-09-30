from collections import deque
import heapq
import sys

def season(tree): #봄여름가을겨울
    deadtree=deque() #영양분이 나무나이보다 적음, 양분이 될 나무들
    age5=deque() #나무나이가 5의 배수인것들
    # print('tree:',tree)
    # print(len(tree))
    tmp=[]
    for _ in range(len(tree)):
        age,x,y=heapq.heappop(tree)
        # print('age,x,y:',age,x,y)
        if nutri[x][y]>=age: #토지의 영양분이 나무 나이보다 크거나 같으면
            nutri[x][y]-=age
            age+=1
            heapq.heappush(tmp,(age,x,y)) #임시큐에 저장하여 기존의 큐가 바뀌지 않고 진행
            if age%5==0:
                age5.append((x,y))
        else: #영양분이 나무나이보다 적음, 다른큐에 저장
            deadtree.append((age,x,y))
            continue
   #죽은나무들이 영양분으로바뀜 여름
    while deadtree:
        age,x,y=deadtree.popleft()
        nutri[x][y]+=age//2
   #나무나이가 5의 배수인것들
    while age5:
        x,y=age5.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n: 
                continue
            heapq.heappush(tmp,(1,nx,ny))
   #영양분 추가
    for i in range(n):
      for j in range(n):
         nutri[i][j]+=A[i][j]
    return tmp
n,m,k=map(int,input().split())
A=[]
for _ in range(n):
    A.append(list(map(int,sys.stdin.readline().split())))

nutri=[[5]*n for i in range(n)]
tree=[ ]
dx=[-1,-1,-1,0,0,1,1,1]
dy=[-1,0,1,-1,1,-1,0,1]
for _ in range(m):
    x,y,age=map(int,sys.stdin.readline().split())
    x,y=x-1,y-1
    heapq.heappush(tree,(age,x,y))

for _ in range(k):
   tree=season(tree)
print(len(tree))
   