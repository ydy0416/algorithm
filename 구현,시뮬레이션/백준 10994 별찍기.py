def sero(i):
    for _ in range(i,k-i):
        graph[_][i]='*'
        graph[_][k-1-i]='*'
        
def garo(i):
    for _ in range(i+1,k-1-i):
        graph[i][_]='*'
        graph[k-1-i][_]='*'

n=int(input())
k=(n-1)*4+1
graph=[['']*k for i in range(k)]
tmp=0
for i in range(0,k//2,2):
    sero(i)
    garo(i)

graph[k//2][k//2]='*'
for i in range(k):
    for j in range(k):
        if graph[i][j]=='*':
            print(graph[i][j], end='')
        else:
            print(' ', end='')
    print()
