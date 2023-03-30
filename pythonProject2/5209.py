# def perm(i,tmp):
#     global res
#     if tmp<res: #백트레킹 이전에 계산한값보다 더 크면 내려가지 않고 반환
#         return
#
#     if i == N:
#         res = min(tmp, res)
#         return
#     else:
#         for j in range(N): #사용하지 않은 숫자를
#             if visited[j] == 0: #방문체크
#                 visited[j] = 1 #j번자리 숫자 사용으로 표시
#                 perm(i+1,tmp+arr[i][j])
#                 visited[j] = 0 #j번자리 숫자를 다른 자리에서 쓸 수 있게 되돌리기
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     res = 100000000
#     visited = [0]*N  # 공장 방문 체크
#     perm(0,0)
#     print(f'#{tc} {res}')



def perm(i,tmp):
    global res
    if tmp>res: #백트레킹
        return

    if i == N:
        res = min(tmp, res)
        return
    else:
        for j in range(N): #사용하지 않은 숫자를
            if visited[j] == 0: #방문체크
                visited[j] = 1 #j번자리 숫자 사용으로 표시
                perm(i+1,tmp+arr[i][j])
                visited[j] = 0 #j번자리 숫자를 다른 자리에서 쓸 수 있게 되돌리기


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    res = 100000000
    visited = [0]*N  # 공장 방문 체크
    perm(0,0)
    print(f'#{tc} {res}')