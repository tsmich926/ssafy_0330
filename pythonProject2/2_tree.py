# 연습문제3

#트리만들기
# N = 12
# V = 13
# 
# strV = '1 2 1 3 2 4 3 5 3 6 4 8 5 8 5 9 6 10 6 11 7 12 11 13'
# 
# lst = list(map(int,strV.split()))
# 
# TREE = [[0,0] for _ in range(V+1)]
# for i in range(0,len(lst),2):
#     p = lst[i]
#     c = lst[i+1]
#     if TREE[p][0]==0:
#         TREE[p][0] = c
#     else:
#         TREE[p][1] = c
# 
# print(TREE)



def preorder(root):
    # 자식이 없으면 처리할 필요없으니까
    if root:
        print(root)
        preorder(TREE[root][0])
        preorder(TREE[root][1])


N = 12
V = 13

strV = '1 2 1 3 2 4 3 5 3 6 4 8 5 8 5 9 6 10 6 11 7 12 11 13'

lst = list(map(int,strV.split()))

TREE = [[0,0] for _ in range(V+1)]
for i in range(0,len(lst),2):
    p = lst[i]
    c = lst[i+1]
    if TREE[p][0]==0:
        TREE[p][0] = c
    else:
        TREE[p][1] = c

print(TREE)
preorder(1)
