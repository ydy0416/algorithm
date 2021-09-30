data=input()
cnt1=0
cnt2=0
chk=True
for i in data:
    if i=='(':
        cnt1+=1
    elif i==')':
        cnt1-=1
    elif i=='[':
        cnt2+=1
    elif i==']':
        cnt2-=1
    if cnt1<0 or cnt2<0:
        chk=False
        break
        