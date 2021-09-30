from collections import deque
data=deque(input())
ans_list=[]
while data:
    tmp=data.popleft()
    if tmp=='q':
        isTrue=True
        for i in ans_list:
            if i[-1]=='k':
                i.append(tmp)
                isTrue=False
                break
        if isTrue:
            ans_list.append([tmp])
    elif tmp=='u':
        for i in ans_list:
            if i[-1]=='q':
                i.append(tmp)
                break
    elif tmp=='a':
        for i in ans_list:
            if i[-1]=='u':
                i.append(tmp)
                break
    elif tmp=='c':
        for i in ans_list:
            if i[-1]=='a':
                i.append(tmp)
                break
    elif tmp=='k':
        for i in ans_list:
            if i[-1]=='c':
                i.append(tmp)
                break
ans=0
isTrue=True
for i in ans_list:
    if len(i)%5==0:
        ans+=1
    else:
        isTrue=False
if isTrue and ans>0:
    print(ans)
else:
    print(-1)