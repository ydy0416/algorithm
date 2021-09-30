# N(1 ≤ N ≤ 1,000) 완전탐색으로 풀기
n=int(input())
data=list(map(int,input().split()))
balloon=[1]*n
balloon[0]=0
idx=0
print(1)
while sum(balloon)!=0:
    i=data[idx]
    cnt=0
    # print('i:',i)
    if i>0:
        while True:
            idx+=1
            if idx>=n: idx=0 #인덱스 범위 초과
            if balloon[idx]!=0:
                cnt+=1
            if cnt==i:
                balloon[idx]=0
                print(idx+1)
                break
    else:
        while True:
            idx-=1
            if idx<0: idx=n-1
            if balloon[idx]!=0:
                cnt+=1
            if cnt==abs(i):
                balloon[idx]=0
                print(idx+1)
                break
