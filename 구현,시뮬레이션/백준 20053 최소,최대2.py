T=int(input())
for _ in range(T):
    n=int(input())
    data=list(map(int,input().split()))
    print(min(data), max(data))