import sys
def left_search(end,num):
    start=0
    while start<=end:
        mid=(start+end)//2
        if data[mid]==num:
            if mid==0: return mid
            if data[mid-1]!=num: return mid
            end=mid-1
        elif data[mid]<num:
            start=mid+1

def right_search(start,num):
    end=n-1
    while start<=end:
        mid=(start+end)//2
        if data[mid]==num:
            if mid==n-1: return mid #현재 인덱스가 마지막일때 
            if data[mid+1]!=num: return mid
            start=mid+1
        elif data[mid]>num:
            end=mid-1

def binary_search(num):
    start=0
    end=n-1
    while start<=end:
        mid=(start+end)//2
        if data[mid]==num: 
            # print('num,mid index=',num,mid)
            # print('left_search',left_search(mid,num))
            # print('right_search',right_search(mid,num))
            return right_search(mid,num)-left_search(mid,num)+1
        elif data[mid]<num: #오른쪽으로 이동
            start=mid+1
        elif data[mid]>num: #왼쪽으로 이동
            end=mid-1
    return 0
n=int(input())
data=list(map(int,sys.stdin.readline().split()))
data.sort()
m=int(input())
search=list(map(int,sys.stdin.readline().split()))

ans=[]
for i in search:
    ans.append(binary_search(i))
for i in ans:
    print(i, end=' ')