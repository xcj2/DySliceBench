
import bisect
import collections
import itertools


def getint(): return int(input())
def getints(): return list(map(int, input().split()))
def getint2d(rows): return [getints() for _ in range(rows)]
def getgrid(rows): return [input() for _ in range(rows)]
def array1d(n, value): return [value for _ in range(n)]
def array2d(n, m, value): return [array1d(m, value) for _ in range(n)]


def partial_sum(xs):
    if not xs:
        return [0]
    ys = [0, xs[0][1]]
    for i in range(1, len(xs)):
        xs[i][1] += xs[i-1][1]
        ys.append(xs[i][1])
    return ys

n,w=getints()
items=getint2d(n)
w0 = items[0][0]
kind0=list(sorted(filter(lambda s: s[0] == w0,     items), reverse=True))
kind1=list(sorted(filter(lambda s: s[0] == w0 + 1, items), reverse=True))
kind2=list(sorted(filter(lambda s: s[0] == w0 + 2, items), reverse=True))
kind3=list(sorted(filter(lambda s: s[0] == w0 + 3, items), reverse=True))

kind0 = partial_sum(kind0)
kind1 = partial_sum(kind1)
kind2 = partial_sum(kind2)
kind3 = partial_sum(kind3)



res = 0

for n0 in range(len(kind0)):
    for n1 in range(len(kind1)):
        for n2 in range(len(kind2)):
            for n3 in range(len(kind3)):
                weight = n0*w0 + n1*(w0+1) + n2*(w0+2) + n3*(w0+3)
                if weight > w: continue
                tmp = kind0[n0] + kind1[n1] + kind2[n2] + kind3[n3]
                res = max(res, tmp)

print(res)
