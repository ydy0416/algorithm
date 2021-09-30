def chk(graph):
    cnt=0
    #가로 체크
    for i in range(5):
        tmp=0
        for j in range(5):
            tmp+=graph[i][j]
        if tmp==0: cnt+=1
    
    #세로체크
    for i in range(5):
        tmp=0
        for j in range(5):
            tmp+=graph[j][i]
        if tmp==0: cnt+=1
    #대각선 체크
    if graph[0][0]+graph[1][1]+graph[2][2]+graph[3][3]+graph[4][4]==0:
        cnt+=1
    if graph[0][4]+graph[1][3]+graph[2][2]+graph[3][1]+graph[4][0]==0:
        cnt+=1
    if cnt>=3:
        
        return True

    return False

def bingo(number,graph):
    breaker=False
    for i in range(5):
        for j in range(5):
            if graph[i][j]==number :
                graph[i][j]=0
                breaker=True
                break
        if breaker==True:
            break
    if chk(graph):
        return True

graph=[]
for i in range(5):
    graph.append(list(map(int,input().split())))

call=[]
for i in range(5):
    call.append(list(map(int,input().split())))

breaker=False
cnt=0
for i in range(5):
    for j in range(5):
        number=call[i][j]
        cnt+=1
        # print(number)
        if bingo(number,graph):
            breaker=True
            break
    if breaker==True:
        break
print(cnt)