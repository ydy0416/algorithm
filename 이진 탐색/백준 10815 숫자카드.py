def binary_search(number):
    start,end=0,n-1
    while start<=end:
        mid=(start+end)//2
        if data[mid]==number:
            return 1
        if number>data[mid]:
            start=mid+1
        else:
            end=mid-1
    return 0
n=int(input())
data=list(map(int,input().split()))
data.sort()
m=int(input())
chk=list(map(int,input().split()))

ans=[]
for i in chk:
    ans.append(binary_search(i))
print(' '.join(map(str,ans)))
