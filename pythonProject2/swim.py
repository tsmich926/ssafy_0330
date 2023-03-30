def solve(price,plan,tmp):
    global res

    solve_1day(price[0])
    solve_1mon(price[1])
    solve_3mon(price[2])
    solve_1year(price[3])



T = int(input())
for tc in range(1,T+1):
    price = list(map(int,input().split()))
    plan = list(map(int,input().split()))
    res = 999


