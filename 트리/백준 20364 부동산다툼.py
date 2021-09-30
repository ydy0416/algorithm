import sys
n,q=map(int,input().split())
owned=[False]*(n+1)
for _ in range(q):
    target=int(sys.stdin.readline())
    tmp=target
    flag=True
    while tmp>0:
        if owned[tmp]==True: #이미 점유된 땅
            last_owned=tmp
            flag=False
        tmp=tmp//2
    if flag:
        print(0)
        owned[target]=True
    else:
        print(last_owned)