n=int(input())
dict={}
ans=0
for i in range(n):
    a,b=map(int,input().split())
    if a not in dict.keys():
        dict[a]=b
        continue
    if dict[a]!=b:
        dict[a]=b
        ans+=1
print(ans)
