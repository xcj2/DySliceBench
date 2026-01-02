from collections import Counter
import sys
def zur(z, xx):
    c = 0
    k = 0
    i = 0
    while True:
        i += 1
        if i in xx:
            c += 1
        else:
            k += 1
        if k == z:
            return z + c

def xxxxx(z, xx):
    if z not in xx:
        return z
    while True:
        z -= 1
        if z == 0:
            print(-1)
            sys.exit()
        if z not in xx:
            return z

def mkxp(xs):
    xp = {}
    for i, x in enumerate(xs):
        i = i+1
        if x > i:
            print(-1)
            sys.exit()
        if x not in xp:
            xp[x] = list()
        xp[x].append(i)
    return xp

i = input()
xs = [int(x) for x in input().strip().split(" ")]
xp = mkxp(xs)


x = max(xs)
xo = []
xx = set()

while True:
    last = len(xs)
    if x == 0:
        break
    nxx = set()
    if x in xp:
        for i in xp[x]:
            xxx = zur(x + last - i, xx)
            xo.append((xxx, x))
            nxx.add(xxx)
        last -= len(xp[x])
    xx = nxx | xx
    xs = [int(i) for i in xs if i != x]
    xp = mkxp(xs)
    x -= 1

for i, x in sorted(xo, key=lambda x:x[0]):
    print(x)
