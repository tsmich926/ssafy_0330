def lomuto(l,r):
    p = r
    i =l-1 #경계지점
    for j in range(l,r): #훑기 큰게 나타나면 하나증가하고 바꾸기
        if lst[j] <  lst[p]:
            i += 1
            lst[i],lst[j] = lst[j],lst[i]

    #끝ㅇㅔ 있는 얘 자기 자리 찾아가게
    i += 1
    lst[i], lst[p] = lst[p], lst[i]

    return i



def quickS(l, r):
    if l < r:
        # p = hoare(l, r)
        p = lomuto(l,r)
        quickS(l, p - 1)
        quickS(p + 1, r)


lst = [3, 2, 4, 6, 9, 1, 8, 7, 5]
quickS(0, 8)
print(lst)


# 하나는 경계점 -1로 두기
# 하나는 전체 훑기용
# 피봇이 5일때