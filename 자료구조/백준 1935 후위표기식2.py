from collections import deque
# 1<=n<=26
n=int(input())
sik=deque(input())

#딕셔너리 생성
dict={chr(i):0 for i in range(65,91)}
start=65
for i in range(n):
    dict[chr(start)]=int(input())
    start+=1

#알파벳 > 숫자변환
for i in range(len(sik)):
    if sik[i]=='+' or sik[i]=='-' or sik[i]=='*' or sik[i]=='/' : continue
    sik[i]=dict[sik[i]]

stack=deque()
while sik:
    tmp=sik.popleft()
    if tmp=='+':
        num1=stack.pop()
        num2=stack.pop()
        num3=num2+num1
        stack.append(num3)
    elif tmp=='-':
        num1=stack.pop()
        num2=stack.pop()
        num3=num2-num1
        stack.append(num3)
    elif tmp=='*':
        num1=stack.pop()
        num2=stack.pop()
        num3=num2*num1
        stack.append(num3)
    elif tmp=='/' :
        num1=stack.pop()
        num2=stack.pop()
        num3=num2/num1
        stack.append(num3)
    else:
        stack.append(tmp)
print('%.2f'%stack[0])




