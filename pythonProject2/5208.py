# def perm(lst,i,tmp):
#     battery = stops[1]
#     global res
#     if res < tmp: #백트레킹
#         return
#
#     if i == num:
#         res = min(res, tmp)
#         return
#     else:
#         perm(충전했을)
#         배터리 증가분-1
#         perm(층전)
#         배터리-1

#
# T = int(input())
# for tc in range(1,T+1):
#     lst = list(map(int,input().split()))
#     num = lst[0]
#     res = 9999
#     stops = lst[1:]
#     perm(1,num,0)


# def par(k):
#     if k==N:
#         print(result)
#         for i in range(N):
#             if result[i]: #1인 경우만 출력
#                 print(nums[i],end=' ')
#         print()
#         return
#
#     result[k] = 1
#     par(k+1)
#     result[k] = 0
#     par(k+1)
#
#
# nums = [7,3,2,1,5]
# N = len(nums)
# result = [-1]*N
# cnt = 0
# par(0)
# print(cnt)

def solve(k,remain,cnt):
    global minV
    if minV <= cnt:
        return

    if k==lst[0]:
        minV = cnt
        return
    if remain==0:
        return


    solve(k+1,lst[k+1],cnt+1)
    solve(k+1,remain-1,cnt)


T = int(input())
for tc in range(1,T+1):
    lst = list(map(int,input().split())) + [0]
    minV =lst[0]

    solve(1,lst[1],0)
    print(f'#{tc} {minV}')
