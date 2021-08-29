from collections import deque
import sys
def operation(ord):
    if ord[0:4]=='push':
        a,b=ord.split()
        if a=='push_back':
            q.append(b)
        elif a=='push_front':
            q.appendleft(b)
    elif ord=='pop_front':
        if len(q)==0: print(-1)
        else: print(q.popleft())
    
    elif ord=='pop_back':
        if len(q)==0: print(-1)
        else: print(q.pop())
    elif ord=='size':
        print(len(q))
    elif ord=='empty':
        if len(q)==0:
            print(1)
        else:
            print(0)
    elif ord=='front':
        if len(q)==0:
            print(-1)
        else:
            print(q[0])
    elif ord=='back':
        if len(q)==0:
            print(-1)
        else:
            print(q[-1])
            

q=deque()
for _ in range(int(input())):
    ord=sys.stdin.readline().rstrip()
    operation(ord)
