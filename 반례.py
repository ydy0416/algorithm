def solve1(n,q,data):
    owned = set()
    for i in data:
        x = i
        node, isOwned, num = x, False, 0
        while node > 0:
            if node in owned:
                isOwned = True
                num = node
            node //= 2
        print(num)
        if not isOwned:
            owned.add(x)
    return owned

def solve2(n,q,data):
    owned=[False]*(n+1)
    ans=[]
    for i in data:
        target=i
        tmp=i
        flag=True
        while tmp>0:
            if owned[tmp]==True: #이미 점유된 땅
                ans.append[tmp]
                flag=False
                break
            tmp=tmp//2
        if flag==True:
            ans.append(0)
            owned[target]=True
    return ans
#랜덤수 배정
import random
while True:
    n=6
    q=4
    data = [random.randrange(1,6) for _ in range(q)]
    print(data)
    v1= solve1(n,q,data)
    v2= solve2(n,q,data)
    if v1 != v2:
        print('data:',data)
        print('v1:',v1)
        print('v2:',v2)
        break
