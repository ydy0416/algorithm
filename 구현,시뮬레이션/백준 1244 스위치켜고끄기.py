n=int(input())
switch=list(map(int,input().split()))
m=int(input())
student=[]
for i in range(m):
    student.append(list(map(int,input().split())))

for i in student:
    gender=i[0]
    number=i[1]
    if gender==1: #남자일경우
        for i in range(number-1,n,number):
            if switch[i]==0:
                switch[i]=1
            else:
                switch[i]=0
    if gender==2:
        dis=1
        idx=number-1
        if switch[idx]==0:
            switch[idx]=1
        else:
            switch[idx]=0
        while True:
            if idx-dis<0 or idx+dis>=n: break
            if switch[idx-dis]==switch[idx+dis]:
                if switch[idx-dis]==0:
                    switch[idx-dis],switch[idx+dis]=1,1
                else:
                    switch[idx-dis],switch[idx+dis]=0,0
                dis+=1
            else:
                break
cnt=0
for i in switch:
    print(i, end=' ')
    cnt+=1
    if cnt%20==0:
        print()
                
            