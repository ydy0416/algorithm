def binary_search():
    start=0
    end=max(wants)
    while start<=end:
        tmp_budget=budget
        mid=(start+end)//2 #상한액
        # print('start,mid,end,tmp_budget:',start,mid,end,tmp_budget)
        for want in wants:
            if want<mid:  #수요금액이 상한액보다 적을 때
                tmp_budget-=want
            else:
                tmp_budget-=mid
            
        if tmp_budget>=0: #다주고 예산이 남을 때 상한액올리기
            ans=mid
            start=mid+1
        else:
            end=mid-1
    return ans

n=int(input())
wants=list(map(int,input().split()))
budget=int(input())

print(binary_search())
