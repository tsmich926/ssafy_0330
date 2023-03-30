# def binaryS(A,keys,key):
#     global cnt
#     m = len(A)//2
#     l = 0
#     r = len(A)-1
#     if A[m] > key : #찾고자 하는 수보다 중간 인덱스의 값이 크면
#         for i in range(l,m):
#             if A[i] == key:
#                 cnt += 1
#             else:
#
#
#     if A[m] == key: #찾고자 하는 값이 중간 인덱스 값일때
#         cnt +=1
#
#     else: #중간 인덱스의 값이 찾는 값보다 더 작을때
#         for i in range(m+1,r+1):
#             if A[i] == key:
#                 cnt += 1
#             else:
#
#
# T = int(input())
# for tc in range(1,T+1):
#     N,M = map(int,input().split())
#     A = list(map(int,input().split()))
#     A.sort()
#     keys = list(map(int,input().split()))
#     cnt = 0
#     for key in keys:
#         if binaryS(A,keys,key):
#             cnt += 1
#
#     print(f'{tc} {cnt}')


#오른쪽일때 오른쪽이면 안된다고 해야한다
#오왼오왼오왼....

# def binSR(key,l,r):
#     ans = 'left'
#     if l>r:
#         return -1
#
#     m = (l+r)//2
#     if lst[m] == key:
#         return ans
#     if lst[m] < key and ans=='left':
#         ans = 'right'
#         return binSR(key,m+1,r)
#
#     else:
#         if ans == 'right':
#         ans ='left'
#         return binSR(key,l,m-1)


def binSR(key,l,r):
    global ans

    if l>r:
        return -1

    m = (l+r)//2
    if lst[m] == key:
        return 1
    if lst[m] < key:
        if ans=='' or ans=='left':
            ans = 'right'
            return binSR(key,m+1,r)
        else:
            return -1
    else:
        if ans =='' or ans=='right':
            ans ='left'
            return binSR(key,l,m-1)
        else:
            return -1


#처음에는 무조건 오른쪽 선택/왼쪽부터 선택하면 무조건 버림
# 재귀해서 오-왼 오오이면 버림

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    lst = list(map(int,input().split()))
    lst.sort()
    keys = list(map(int,input().split()))
    cnt = 0
    l = 0
    r = len(lst)-1
    for key in keys:
        ans = ''
        if binSR(key,l,r)==1:
            cnt += 1

    print(f'#{tc} {cnt}')
