def sol(index,depth):
    node=data[index]
    

data=[]
while True:
    try:
        data.append(int(input()))
    except:
        break
preorder=[]
sol(0,0)
