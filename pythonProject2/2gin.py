# lst = [2,4,7,9,11,19,23]
# def binS(key):
#     l = 0
#     r = len(lst)-1
#     while l <= r:
#         m = (l+r)//2
#         if lst[m] == key:
#             return m
#         if lst[m] < key:
#             l = m+1
#         else:
#             r = m-1
#     return -1
#
# print(binS(7))
# print(binS(23))
# print(binS(1))
# print(binS(24))



lst = [2,4,7,9,11,19,23]
def binSR(key,l,r):
    global res

    if l>r:
        return -1

    m = (l+r)//2
    if lst[m] == key:
        # result= m
        return m
    if lst[m] < key:
        return binSR(key,m+1,r)

    else:
        return binSR(key,l,m-1)


def binS(key):
    l = 0
    r = len(lst)-1
    while l <= r:
        m = (l+r)//2
        if lst[m] == key:
            return m
        if lst[m] < key:
            l = m+1
        else:
            r = m-1
    return -1


N =len(lst)

print(binSR(7,0,N-1))

print(binSR(23,0,N-1))

print(binSR(1,0,N-1))

print(binSR(24,0,N-1))

