import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def LI(): return list(map(int, input().split()))
def LIR(row,col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [list(map(str, input().split())) for _ in range(row)]
        return map(list, zip(*read_all))

#################

N = I()
X,Y,U = LIR(N,3)
X = [int(x) for x in X]
Y = [int(y) for y in Y]

d1 = defaultdict(lambda:defaultdict(list))
d2 = defaultdict(lambda:defaultdict(list))

u = defaultdict(list)
r = defaultdict(list)
d = defaultdict(list)
l = defaultdict(list)

for i in range(N):
    if U[i] == 'U':
        u[X[i]].append(Y[i])
    elif U[i] == 'D':
        d[X[i]].append(Y[i])
    elif U[i] == 'R':
        r[Y[i]].append(X[i])
    else:
        l[Y[i]].append(X[i])

for k in u.keys():
    u[k].sort()

for k in d.keys():
    d[k].sort()

for k in r.keys():
    r[k].sort()

for k in l.keys():
    l[k].sort()

for i in range(N):
    d1[U[i]][Y[i]-X[i]].append(X[i])
    d2[U[i]][Y[i]+X[i]].append(X[i])

ans = float('inf')
for i in range(N):
    if U[i] == 'U':
        p = bisect_left(d[X[i]],Y[i])
        if p <= len(d[X[i]])-1 and len(d[X[i]]):
            ans = min(ans,(d[X[i]][p]-Y[i])*5)

        p = bisect_left(d1['L'][Y[i]-X[i]],X[i])
        if p <= len(d1['L'][Y[i]-X[i]])-1 and len(d1['L'][Y[i]-X[i]]):
            ans = min(ans,(d1['L'][Y[i]-X[i]][p]-X[i])*10)  

        p = bisect_left(d2['R'][Y[i]+X[i]],X[i])
        if 0 <= p-1 <= len(d2['R'][Y[i]+X[i]])-1 and len(d2['R'][Y[i]+X[i]]):
            ans = min(ans,(X[i]-d2['R'][Y[i]+X[i]][p-1])*10)

    elif U[i] == 'D':
        p = bisect_left(u[X[i]],Y[i])
        if 0 <= p-1 <= len(u[X[i]])-1 and len(u[X[i]]):
            ans = min(ans,(Y[i]-u[X[i]][p-1])*5)

        p = bisect_left(d1['R'][Y[i]-X[i]],X[i])
        if 0 <= p-1 <= len(d1['R'][Y[i]-X[i]])-1 and len(d1['R'][Y[i]-X[i]]):
            ans = min(ans,(X[i]-d1['R'][Y[i]-X[i]][p-1])*10)       

        p = bisect_left(d2['L'][Y[i]+X[i]],X[i])
        if p <= len(d2['L'][Y[i]+X[i]])-1 and len(d2['L'][Y[i]+X[i]]):
            ans = min(ans,(d2['L'][Y[i]+X[i]][p]-X[i])*10)

    elif U[i] == 'R':
        p = bisect_left(l[Y[i]],X[i])
        if p <= len(l[Y[i]])-1 and len(l[Y[i]]):
            ans = min(ans,(l[Y[i]][p]-X[i])*5)

        p = bisect_left(d1['D'][Y[i]-X[i]],X[i])
        if p <= len(d1['D'][Y[i]-X[i]])-1 and len(d1['D'][Y[i]-X[i]]):
            ans = min(ans,(d1['D'][Y[i]-X[i]][p]-X[i])*10)       

        p = bisect_left(d2['U'][Y[i]+X[i]],X[i])
        if p <= len(d2['U'][Y[i]+X[i]])-1 and len(d2['U'][Y[i]+X[i]]):
            ans = min(ans,(d2['U'][Y[i]+X[i]][p]-X[i])*10)

    else:
        p = bisect_left(r[Y[i]],X[i])
        if 0 <= p-1 <= len(r[Y[i]])-1 and len(r[Y[i]]):
            ans = min(ans,(X[i]-r[Y[i]][p-1])*5)

        p = bisect_left(d1['U'][Y[i]-X[i]],X[i])
        if 0 <= p-1 <= len(d1['U'][Y[i]-X[i]])-1 and len(d1['U'][Y[i]-X[i]]):
            ans = min(ans,(X[i]-d1['U'][Y[i]-X[i]][p-1])*10)

        p = bisect_left(d2['D'][Y[i]+X[i]],X[i])
        if 0 <= p-1 <= len(d2['D'][Y[i]+X[i]])-1 and len(d2['D'][Y[i]+X[i]]):
            ans = min(ans,(X[i]-d2['D'][Y[i]+X[i]][p-1])*10)


if ans == float('inf'):
    print('SAFE')
else:
    print(ans)