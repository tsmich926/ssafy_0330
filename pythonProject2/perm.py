def perm(i,k):
    if i == k:
        print(*p)
    else:
        for j in range(k): #사용하지 않은 숫자를
            if used[j] == 0: #used에서 순서대로 검색
                p[i] = A[j]
                used[j] = 1 #j번자리 숫자 사용으로 표시
                perm(i+1,k)
                used[j] = 0 #j번자리 숫자를 다른 자리에서 쓸 수 있게 되돌리기


A = [1,2,3]
p = [0] * 3
used = [0] * 3

perm(0,3)


# def dfs(i, tmp):  # 행, 현재 타임 합
#     global res
#     if tmp >= res:
#         return
#     if i == N:
#         res = min(tmp, res)
#         return
#
#     for j in range(N):
#         if not visited[j]:
#             visited[j] = 1
#             dfs(i+1, tmp+a[i][j])
#             visited[j] = 0
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     a = [list(map(int, input().split())) for _ in range(N)]
#     res = 987654321
#     visited = [0]*N  # 열 방문 체크
#     dfs(0, 0)
#     print("#{} {}".format(tc, res))