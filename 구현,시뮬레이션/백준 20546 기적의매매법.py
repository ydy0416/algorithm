def jh(cash,data):
    amount=0
    for i in range(13):
        if cash>=data[i]:
            amount+=cash//data[i]
            cash%=data[i]
    return cash+amount*data[13]

def sm(cash,data):
    amount=0
    #cnt1= + cnt2= -
    cnt1=0
    cnt2=0
    yesterday=data[0]
    for i in range(13):

        #주가 상승
        if yesterday<data[i]:
            cnt1+=1
            cnt2=0
            yesterday=data[i]
        #주가 하락
        elif yesterday>data[i]:
            cnt2+=1
            cnt1=0
            yesterday=data[i]
        #주식판매
        if cnt1>=3:
            cash+=amount*data[i]
            amount=0
            
        #주식 구매
        elif cnt2>=3:
            amount+=cash//data[i]
            cash%=data[i]
        # print('주식날짜, 주식보유, 현금',i+1,amount,cash)
    
    return cash+amount*data[13]

cash=int(input())
data=list(map(int,input().split()))

tmp=jh(cash,data)
tmp2=sm(cash,data)
if tmp>tmp2:
    print('BNP')
elif tmp<tmp2:
    print('TIMING')
else:
    print('SAMESAME')
