import math
def segmentTree(dat, f, sentinel):
        pad = 2 ** math.ceil(math.log(len(dat),2))
        dat = [0] * pad + dat + [sentinel] * (pad - len(dat))
        for i in range(pad - 1, 0, -1):
            dat[i] = f(dat[i * 2],dat[i * 2 + 1])
        return dat

def get_lr(b,d):
    l = r = 0
    while r < len(b):
        while b[l] + d < b[r]:
            l += 1
        for r in range(r,len(b)):
            if b[l] + d < b[r]:
                r -= 1
                break
        r += 1
        yield l,r
        l += 1
    
import sys
f = sys.stdin

_, d = map(int, f.readline().split())

xyb = []
for line in f:
    xyb.append(tuple(map(int, line.split())))
from operator import itemgetter
xyb.sort(key=itemgetter(2))

x = [xybi[0] for xybi in xyb]
y = [xybi[1] for xybi in xyb]
b = [xybi[2] for xybi in xyb]

xmax = segmentTree(x,max,sentinel = 0)
xmin = segmentTree(x,min,sentinel = 2000000)
ymax = segmentTree(y,max,sentinel = 0)
ymin = segmentTree(y,min,sentinel = 2000000)


pad = len(xmax) // 2
max_size = 0
def create_index(l,r):
    index = []
    ia = index.append
    while l < r:
        if r & 1:
            r -= 1
            ia(r)
        if l & 1:
            ia(l)
            l += 1
        l >>= 1
        r >>= 1
    return index

for l,r in get_lr(b,d):
    l += pad 
    r += pad
    index = create_index(l,r)

    now_xmax = max(xmax[i] for i in index)
    now_ymax = max(ymax[i] for i in index)
    if max_size < now_xmax * now_ymax:
        max_size = max(max_size,((now_xmax - min(xmin[i] for i in index)) * (now_ymax - min(ymin[i] for i in index))))
print(max_size)