def hoare(l,r):
    p = l
    lp = l+1
    rp =r
    while lp <=rp: #역전되면 끝냄
        while lp<=rp and lst[lp] <= lst[p]: #첫번째에 무한히 가지않도록 하는 조건 추가
            lp += 1
        while lp<=rp and lst[rp] >= lst[p]:
            rp-=1
        #바꿀게 있거나 역전하거나
        if lp<rp:
            lst[lp],lst[rp]=lst[rp],lst[lp] #교환
        #교차
    lst[p],lst[rp] = lst[rp],lst[p]
    
    return rp #반드시 위치를 리턴
        

    return

def quickS(l,r):
    if l<r:
        p = hoare(l,r)
        quickS(l,p-1)
        quickS(p+1,r)


lst = [3,2,4,6,9,1,8,7,5]
quickS(0,8)
print(lst)
# 피봇이 3인 경우
# [(2,1),3,(....)] partition
# ( 좌) (우) 퀵소트함