def merge(left,right):
    global cnt
    result = []
    lp = 0
    rp = 0

    if left[-1] > right[-1]:
        cnt += 1

    while lp<len(left) and rp<len(right): #두개 둘다 사이즈보다 작아야함
        if left[lp] < right[rp]:
            result.append(left[lp])
            lp += 1
        else:
            result.append(right[rp])
            rp += 1
    #둘중 하나라도 떨어진 경우 나머지 부분을 붙여준다
    #extend 리스트 뒤에 리스트 붙이기
    result.extend(left[lp:])
    result.extend(right[rp:])

    return result


def mergeS(lst):
    if len(lst) == 1:
        return lst

    m = len(lst)//2
    left = lst[:m]
    right = lst[m:len(lst)]


    left = mergeS(left)
    right = mergeS(right)
    return merge(left,right)



# lst = [69,10,30,2,16,8,31,22]
# res = mergeS(lst)
# print(res)
#원본데이터는 손대지 않고 sort한 결과 출력

T = int(input())
for tc in range(1,T+1):
    cnt = 0
    N = int(input())
    lst = list(map(int,input().split()))
    res = mergeS(lst)
    ans1 = res[N//2]

    print(f'#{tc} {ans1} {cnt}')