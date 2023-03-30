# import sys
# sys.stdin = open(,"r")


def hoare(A,l,r):
    pivot = A[l] #맨 왼쪽원소기준
    i = l   #피봇보다 큰값을 찾아 오른쪽으로 이동
    j = r   #피봇보다 작은값을 찾아 왼쪽으로 이동
    #두개가 교차하지 않은 상태면
    while j<=j:
        while i<=j and A[i]<=pivot:
            i += 1
        while i<=j and A[j]>=pivot: #피봇보다 작은 얘를 찾아서 왼쪽으로감
            j -= 1
        if i < j: #교차되지 않은 상태로 종료
            A[i],A[j] = A[j],A[i]

    A[j],A[l] = A[l],A[j]
    return j



def qsort(A,l,r):
    if l < r:
        s = hoare(A,l,r)
        qsort(A,l,s-1)
        qsort(A,s+1,r)




T  =int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    qsort(arr,0,N-1)
    print(arr[500000])