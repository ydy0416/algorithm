n,m=map(int,input().split())
bulb=list(map(int,input().split()))
for i in range(m):
    operator=list(map(int,input().split()))
    if operator[0]==1:
        bulb[operator[1]-1]=operator[2]
    elif operator[0]==2:
        for i in range(operator[1]-1,operator[2]):
            if bulb[i]==1:
                bulb[i]=0
            else:
                bulb[i]=1
    elif operator[0]==3:
        for i in range(operator[1]-1,operator[2]):
            bulb[i]=0
    elif operator[0]==4:
        for i in range(operator[1]-1,operator[2]):
            bulb[i]=1
for i in bulb:
    print(i, end=' ')