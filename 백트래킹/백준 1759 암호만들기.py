from itertools import combinations 
l,c=map(int,input().split())
data=list(input().split())
data1=[]
data2=[]
for i in data:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        data1.append(i)
    else:
        data2.append(i)
ans=[]
a=1
b=l-a
# print('data1, data2:', data1,data2)
while b>1:
    data3=list(combinations(data1,a))
    data4=list(combinations(data2,b))
#     print('data1, data2:', data1,data2)
    for i in data3:
        tmp=list(i)
        for k in data4:
            t=tmp+list(k)
            t.sort()
            ans.append(t)
    
    a+=1
    b=l-a
ans.sort()
for i in ans:
    print(''.join(i))