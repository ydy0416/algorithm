from itertools import combinations
n,s=map(int,input().split())
data=list(map(int,input().split()))
ans=0
for i in range(1,n+1):
    tmp=list(combinations(data,i))
    for comb in tmp:
        if sum(comb)==s:
            ans+=1
print(ans)
