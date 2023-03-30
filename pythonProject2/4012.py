#조합
# T = [i for i in 6]
# A = [2,3,4]
# B = list(set(T)-set(A))
# print(B)
# print(T)

def comb(k,M,s):
    global minV
    if k ==M:
        B = list(set(T) - set(A))
        g = abs(calc(A)-calc(B))
        # SA= calc(A)
        # SB = calc(B)
        if minV > g:
            minV = g
        # print(A,B,T)
        return

    for i in range(s,N-M+k+1):
        A[k] = i
        comb(k+1,M,i+1)


def calc(arr):
    sumV = 0
    for i in arr:
        for j in arr:
            sumV += S[i][j]
    return sumV




T = int(input())
for tc in range(1,T+1):
    N = int(input())
    S =[list(map(int,input().split())) for _ in range(N)]


    M = N//2
    T = [i for i in range(N)]
    A = [-1]*M
    minV = 20000*16*16
    comb(0,M,0)
    print(f'#{tc} {minV}')