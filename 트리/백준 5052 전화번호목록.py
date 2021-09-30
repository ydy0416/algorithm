# 1<=t<=50 1<=n<=10000
T=int(input())
for _ in range(T):
    n=int(input())
    data=[]
    isTrue=True
    for i in range(n):
        data.append(input()) #문자열로 받아야함
    data.sort()
    for i in range(n-1):
        num1=data[i]
        num2=data[i+1]
        if num1==num2[0:len(num1)]:
            isTrue=False
            break
    if isTrue:
        print('YES')
    else:
        print('NO')
    