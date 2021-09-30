# 한 줄에 쇠막대기와 레이저의 배치를 나타내는 괄호 표현이 공백없이 주어진다.
#  괄호 문자의 개수는 최대 100,000이다. 
n=input()
new_n=[]
skip=False
for i in range(len(n)):
    if skip==True: 
        skip=False
        continue
    if n[i]=='(' and n[i+1]==')':
        new_n.append('R')
        skip=True
        continue
    else:
        new_n.append(n[i])
stick=0
ans=0      
for i in new_n:
    if i=='(':
        stick+=1
    elif i==')':
        stick-=1
        ans+=1
    elif i=='R':
        ans+=stick
print(ans)
