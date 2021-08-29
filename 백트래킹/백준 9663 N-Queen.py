def dfs(queen,row):
    global ans
    if row==n:
        ans+=1
        return
    for col in range(n):
        queen[row]=col
        #같은 열 있는지 탐색
        for i in range(row):
            if queen[i]==queen[row]:
                break
    
            if abs(queen[i]-queen[row])==row-i:
                break
        else:
            dfs(queen,row+1)
        
n=int(input())
ans=0
for i in range(n):
    queen=[0]*n
    queen[0]=i
    dfs(queen,1)
print(ans)
