# 원소의 합이 10인 부분집합을 모두 출력하시오
# {1,2,3,4,5,6,7,8,9,10}


def f(i,k,s,key,rs):
    global cnt
    global c
    if s == key:
        cnt += 1
    elif i==k or s>key or s+rs<key:
        return
    else:
        bit[i] = 0
        f(i+1,k,s,key,rs-A[i]) #A[i]미포함
        bit[i]=1
        f(i + 1, k, s+A[i], key),rs-A[i]



A = [i for i in range(1,11)]
N = 10
bit[0]*N
key = 10
cnt = 0
c = 0
f(0,N,0,key,sum(A))
print(cnt,c)