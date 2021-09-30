T=int(input())
for _ in range(T):
    n=int(input())
    A=[]
    for i in range(n):
        a,b=map(int,input().split())
        A.append([a,b,a+b])
    A=sorted(A,key=lambda x:x[2])
    ans=n
    for i in range(n):
        x,y,z=A[i][0],A[i][1],A[i][2]
        for j in range(i):
            tmp1,tmp2,tmp3=A[j][0],A[j][1],A[j][2]
            if tmp3>=z: break
            if x>tmp1 and y>tmp2:   
                ans-=1
                break
    print(ans)