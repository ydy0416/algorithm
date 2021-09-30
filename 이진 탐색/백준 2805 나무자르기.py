def binary_search():
    start,end=0,max(data)
    while start<=end:
        mid=(start+end)//2
        # print('start,mid,end:',start,mid,end)
        total=0
        for i in data:
            if i>mid:
                tmp=i-mid
                total+=tmp
        if total==m:
            return mid
        elif total>m : #가져가는 나무길이가 원하는 길이보다 클 때 높이를 올려야한다
            start=mid+1
            ans=mid
        elif total<m: 
            end=mid-1
            
    return ans



n,m=map(int,input().split())
data=list(map(int,input().split()))
print(binary_search())