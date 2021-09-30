n=int(input())
dict={}
for i in range(n):
    a,b=input().split('.')
    if b not in dict:
        dict[b]=1
    else:
        dict[b]+=1
ans=[]
for a,b in dict.items():
    ans.append([a,str(b)])
ans.sort()
for i in ans:
    tmp=' '.join(i)
    print(tmp)