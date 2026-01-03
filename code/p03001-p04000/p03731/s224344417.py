
import bisect
import collections
import itertools

def getint(): return int(input())
def getints(): return list(map(int, input().split()))
def getint2d(rows): return [getints() for _ in range(rows)]
def getgrid(rows): return [input() for _ in range(rows)]
def array1d(n, value): return [value for _ in range(n)]
def array2d(n, m, value): return [array1d(m, value) for _ in range(n)]

n,t=getints()
ts=getints()

segm = [[s,s+t] for s in ts]

update = True
while update:
    update = False
    new_segm = [segm[0]]
    for i in range(1, len(segm)):
        if new_segm[-1][1] >= segm[i][0]:
            new_segm[-1][1] = segm[i][1]
            update = True
        else:
            new_segm.append(segm[i])
    segm = new_segm

res = 0
for s in segm:
    res += s[1] - s[0]

print(res)
