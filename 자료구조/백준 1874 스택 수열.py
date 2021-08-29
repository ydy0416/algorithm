def solve(target):
    global now
    #스택에 아무것도 없을 때
    if len(stack)==0:
        stack.append(now)
        ans.append('+')
        now+=1
    while True:
        if len(stack)==0: return False
        #스택 마지막 값이 타겟과 같을 때
        if stack[-1]==target:
            stack.pop()
            ans.append('-')
            return
    
    #스택 마지막값이 타겟보다 작을 때
        elif stack[-1]<target:
            if now>target: return False
            while stack[-1]<target:
                stack.append(now)
                now+=1
                ans.append('+')
        
    #스택 마지막값이 타겟보다 클 때
        elif stack[-1]>target:
            
            while stack[-1]>target and len(stack)>0:
                stack.pop()
                ans.append('-')
                if len(stack)==0:
                    break
    
n=int(input())
data=[]
for i in range(n):
    data.append(int(input()))
now=1
stack=[]
ans=[]
for i in range(len(data)):
    target=data[i]
    flag=solve(target)
    if flag==False:
        break
if flag==False:
    print('NO')
else:
    for i in ans:
        print(i)
    