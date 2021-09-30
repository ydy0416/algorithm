import sys
def binary_search(num):
    start=0
    end=len(section)-1

    while start<=end:
        mid=(start+end)//2
        if num<=int(section[mid][1]): #입력받은 숫자가 mid구간보다 작을 때, 왼쪽으로 이동
            end=mid-1
            ans=section[mid][0]
        else: #입력받은 숫자가 mid구간보다 클 때, 오른쪽으로 이동
            start=mid+1
    return ans

n,m=map(int,input().split())
section=[]

for i in range(n):
    a,b=sys.stdin.readline().split()
    section.append([a,b])   

# section=sorted(section, key=lambda x:x[1])

for i in range(m):
    num=int(sys.stdin.readline())
    print(binary_search(num))
