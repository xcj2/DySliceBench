import sys,bisect

sys.setrecursionlimit(10000000)
N = int(input())
C = [int(input()) for _ in range(N)] #color
v = 10**9+7
from collections import defaultdict
d = defaultdict(list)
for i,c in enumerate(C):
    d[c].append(i)


def guchoku(l):
    assert isinstance(l,list)
    if len(l) <=2:
        return 1
    top_coor = l[0]
    if top_coor in l[1:] and l[0] != l[1]:
        _index= l[1:].index(top_coor)
        return guchoku(l[_index+1:])+ guchoku(l[1:])
    return guchoku(l[1:])

cache = dict()
cache[N] = 1
cache[N-1] = 1
cache[N-2] = 1

def check(i):
    index = bisect.bisect_left(d[C[i]],i+1)

    if index==len(d[C[i]]):
        return -1
    # print(i, d[C[i]] ,d[C[i]][index])
    return d[C[i]][index]

def guchoku_i(i):
    # print("hoge",i,d[C[i]])
    if i<0:
        raise
    if i in cache:
        return cache[i]
    c = check(i)
    if C[i] != C[i+1] and c !=-1 :
        cache[i]= guchoku_i(i+1) + guchoku_i(c) %v
        return cache[i]
    cache[i]=  guchoku_i(i+1) %v
    return cache[i]

# print(guchoku(C))
print(guchoku_i(0)%v )