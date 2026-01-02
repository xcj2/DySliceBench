class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

def bsearch(mn, mx, func):
    #func(i)=True を満たす最大のi (mn<=i<mx)
    idx = (mx + mn)//2
    while mx-mn>1:
        if func(idx):
            idx, mn = (idx + mx)//2, idx
            continue
        idx, mx = (idx + mn)//2, idx
    return idx

import sys;input=sys.stdin.readline
Q, = map(int, input().split())
qs = []
c = 0
j = 0
for _ in range(Q):
    q = input().split()
    if len(q) == 1:
        c += 1
    else:
        a, b = int(q[1]), int(q[2])
        qs.append((a, b, c, j))
        c = 0
        j+=1
if c:
    qs.append((a, b, c, j))

m = j
qqs = sorted(qs, key=lambda x:x[0])
j2i = dict()
i2a = dict()
for i, (a, b, c, j) in enumerate(qqs):
    j2i[j] = i+1
    i2a[i+1] = a

m = len(j2i)
st = Bit(m)
st_sum = Bit(m)
asum=bsum=0
#print(i2a)
#print(j2i)
for a, b, c, i in qs:
    if c:
        j = bsearch(0, m+1, lambda x: st.sum(x)<ci)
#        print(st_sum.sum(j+1))
        for _ in range(c):
            if not i%2:
                print(i2a[j+1], -2*st_sum.sum(j+1)+asum+bsum)
            else:
                print(i2a[j+1], -st_sum.sum(j)+(asum-st_sum.sum(j+1))+bsum)
    asum += a
    bsum += b
    st.add(j2i[i], 1)
    st_sum.add(j2i[i], a)
    ci = -(-(i+1)//2)
