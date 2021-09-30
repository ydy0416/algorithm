def recursion(s,e,depth):
    if depth==k-1: 
        return
    root=(s+e)//2
    ans[depth].append(data[root])
    data[root]=0
    recursion(s,root-1,depth+1)
    recursion(root+1,e,depth+1)

k=int(input())
data=list(map(int,input().split()))
ans=[[] for i in range(k)]
recursion(0,len(data)-1,0)
for i in data:
    if i!=0:
        ans[k-1].append(i)
for i in ans:
    for j in i:
        print(j, end=' ')
    print()