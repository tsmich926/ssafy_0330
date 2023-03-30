def merge(left,right):
    m = (l+r)//2
    result = []
    lp =l
    rp = m+1


    while lp<=m and rp<=r: #두개 둘다 사이즈보다 작아야함

        if left[lp] < right[rp]:
            result.append(left[lp])
            lp += 1
        else:
            result.append(right[rp])
            rp += 1

    while lp <= m :
        result.append(lst[lp])
        lp += 1

    while rp <= r:
        result.append(lst[rp])
        rp +=1
    #둘중 하나라도 떨어진 경우 나머지 부분을 붙여준다
    #extend 리스트 뒤에 리스트 붙이기
    result.extend(left[lp:])
    result.extend(right[rp:])

    return result


def mergeS(lst):
    if len(lst) == 1:
        return lst


    m = len(lst)//2
    # left = lst[:m]
    # right = lst[m:len(lst)]

    mergeS(l,m)
    mergeS(m+1,r)
    merge(l,r)


lst = [69,10,30,2,16,8,31,22]
res = mergeS(lst)
print(res)
#원본데이터는 손대지 않고 sort한 결과 출력
