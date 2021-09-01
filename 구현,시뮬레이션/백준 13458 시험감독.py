# 첫째 줄에 시험장의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다.
# 둘째 줄에는 각 시험장에 있는 응시자의 수 Ai (1 ≤ Ai ≤ 1,000,000)가 주어진다.
# 셋째 줄에는 B와 C가 주어진다. (1 ≤ B, C ≤ 1,000,000)
n=int(input())
data=list(map(int,input().split()))
b,c=map(int,input().split())
cnt=0
for i in range(n):
    data[i]-=b
    cnt+=1
    if c==0: continue
    if data[i]<0: continue
    cnt+=data[i]//c
    data[i]%=c
    if data[i]>0:
        cnt+=1
print(cnt)
