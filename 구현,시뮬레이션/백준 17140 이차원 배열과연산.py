def row_chk(A):   #행 정렬하여 갯수세기
    i=0
    row_max=0
    for i in range(100):
        if A[i][0]==0: break
        tmp=set(A[i])
        tmp.remove(0)
        row_max=max(row_max,len(tmp))
        print('tmp,len:',tmp,len(tmp))
    return row_max

def col_chk(A):
    i=0
    col_max=0
    for i in range(100):
        if A[0][i]==0: break
        tmp=[]
        for j in range(100):
            if A[j][i]==0: break
            tmp.append(A[j][i])
        tmp=set(tmp)
        col_max=max(col_max,len(tmp))
        print('tmp,len:',tmp,len(tmp))
    return col_max 

r,c,k=map(int,input().split())
A=[[0]*10 for i in range(10)]
for i in range(3):
    A[i][0],A[i][1],A[i][2]=map(int,input().split())

while A[9][9]==0:
    row_cnt=row_chk(A)
    col_cnt=col_chk(A)
    if row_cnt>=col_cnt: #행의 갯수가 열의 갯수보다 같거나 크다
        #행연산
        for i in range(100):
            if A[i][0]==0: break
            tmp=A[i]
            tmp.sort()
            tmp.remove(0)
            print('tmp:',tmp)
            
            dict={}
            for j in tmp:
                if j not in dict:
                    dict[j]=1
                    continue
                dict[j]+=1
        print(dict)

    break

#1. 먼저 r,c연산 중 어떤 연산을 해야할지 비교 > 종류가 많아야 함, 갯수상관x

# for i in A:
#     print(i)