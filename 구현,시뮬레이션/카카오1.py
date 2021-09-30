#1번
def solution(id_list, report, k):
    
    data=[]
    for i in id_list:
        data.append([i])
    
    dict={}
    #딕셔너리
    for i in id_list:
        dict[i]=0
    report=list(set(report))
    for i in report:
        a,b=i.split()
        for j in range(len(id_list)):
            if data[j][0]==str(a):
                if b not in data[j]:
                    data[j].append(b)
                    dict[b]+=1
    for i in range(len(data)):
        data[i].append(0)
    
    for a,b in dict.items():
        if b>=k:
            for i in range(len(data)):
                for j in range(1,len(data[i])):
                    if a == data[i][j]:
                        data[i][-1]+=1
    ans=[]
    for i in range(len(data)):
        ans.append(data[i][-1])
                        
    return ans


#2번
import string
def is_prime_number(x):
    print('x:',x)
    print(type(x))
    for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

tmp = string.digits+string.ascii_lowercase
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]
    
def solution(n, k):
    s=convert(n,k)
    s=s.split('0')
    ans=0
    
    for i in s:
        if len(i)==0: continue
        if int(i)<2 : continue
        if is_prime_number(int(i)):
            ans+=1
    
    return ans

#3번
def solution(fees, records):
    answer = []
    car_in={}
    car_time={} #누적시간
    car_fee=[]
    for i in records:
        a,b,c=i.split() #들어온 시간, 차번호, 출입유무
        if b not in car_in.keys():
            car_in[b]=9999
            car_time[b]=0
        if c=='IN':
            d,e=map(int,a.split(':'))
            car_in[b]=d*60+e
        elif c=='OUT':
            d,e=map(int,a.split(':'))
            tmp=d*60+e
            car_time[b]+=(tmp-car_in[b])
            car_in[b]=9999
    print('car_in:',car_in)
    print('car_time:',car_time)
    #23:59분되도 안나간 차들 계산
    for a,b in car_in.items():
        if b!=9999:
            car_time[a]+=(23*60+59)-b
            car_in[a]=9999
    
    
    #요금계산
    for a,b in car_time.items(): #a=차번호 b=누적시간
        if b<fees[0]: #기본시간보다 적을때
            fee=fees[1]
        else:
            fee=fees[1] #기본요금
            b-=fees[0]
            if b%fees[2]>0:
                fee+=(b//fees[2]+1)*fees[3]
            else:
                fee+=(b//fees[2])*fees[3]
        answer.append([a,fee])
    answer.sort()
    ans=[]
    for i in range(len(answer)):
        ans.append(answer[i][1])
    
    return ans

#5.
shp=0
wol=0
def dfs(node,sheep, wolf,visited,graph,info):
    global shp, wol
    if sheep<=wolf:
        return 
    for i in graph[node]:
        if visited[i]==True: continue
        visited[i]=True
        shp=sheep
        wol=wolf
        if info[i]==0: sheep+=1
        else : wolf+=1
        dfs(i,sheep,wolf,visited,graph,info)
        visited[i]=False
    return shp,wol  

def solution(info, edges):
    global shp, wol
    answer = 0
    sheep=0
    wolf=0
    graph=[[] for i in range(len(info))]
    for i in edges:
        a,b=i[0],i[1]
        graph[a].append(b)
    print('graph:', graph)
    visited=[False]*len(info)
    shp,wol=dfs(graph[0][0],0,0,visited,graph,info)
    print('sheep,wolf',shp,wol)
    dfs(graph[0][1],shp,wol,visited,graph,info)
    ans=shp
    visited=[False]*len(info)
    dfs(graph[0][1],0,0,visited,graph,info)
    dfs(graph[0][0],shp,wol,visited,graph,info)
    if ans<shp:
        ans=shp
    ans+=1
    print(ans)
    return answer 