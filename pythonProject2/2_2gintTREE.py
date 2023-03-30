def insert(value):
    root =1
    #값이 있는 동안 빈공간을 찾아서 내려감
    while TREE[root]!=0:
        if TREE[root] > value:
            root *= 2
        else:
            root = root*2+1
    TREE[root] =value



def search(key,root):
    #return 에 value가 있을때는 위로 결과를 올려줘야 한다
    if TREE[root] == 0:
        return -1

    if TREE[root] == key:
        return root
    if TREE[root] <key: #오른쪽 트리로 보냄
        return search(key,root*2+1)
    else:
        return search(key, root * 2)


# TREE = [0,9,4,12,3,6,0,15,0,0,0,0,13,17]
lst = [9,4,12,3,6,15,13,17]
TREE = [0]*100
# p = 1, c1=p*2 ,c2=p*2+1

for v in lst:
    insert(v)
print(TREE)
print(search(12,1))
print(search(14,1))