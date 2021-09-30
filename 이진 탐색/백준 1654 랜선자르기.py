def binary_search():
    start=1
    end=max(data)
    while start<=end:
        mid=(start+end)//2
        # print('start,mid,end:',start,mid,end)
        total=0
        for i in data:
            total+=i//mid
        # print('total:',total)
        if total>=n: #만든 랜선이 필요만큼, 랜선의 길이 늘림    
            start=mid+1
            ans=mid
        elif total<n: #만든 랜선이 필요보다 작음, 왼쪽으로 이동
            end=mid-1
       
    return ans

k,n=map(int,input().split())
data=[]
for i in range(k):
    data.append(int(input()))
# print('data:',data)
print(binary_search())
