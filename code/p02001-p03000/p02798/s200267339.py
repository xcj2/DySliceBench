
from collections import defaultdict
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

def tento(xs):
    bit = Bit(max(xs)+1)
    ans = 0
    for i, p in enumerate(xs):
        ans += i-bit.sum(p)
        bit.add(p, 1)
    return ans
N = int(input())
xs = list(map(int, input().split()))
ys = list(map(int, input().split()))
us = []
vs = []
for i in range(N):
    a, b = xs[i], ys[i]
    if i%2:
        us.append((a,i))
        vs.append((b,i))
    else:
        us.append((b,i))
        vs.append((a,i))
vs.sort()
r = 10**18
for i in range(2**N):
    t = 0
    tt = 0
    rs = [0]*N
    rs2 = [0]*(N//2)
    for j in range(N):
        if i%2:
            if 2*t < N:
                rs[t*2] = vs[j]
            t += 1
        else:
            if 2*tt+1 < N:
                rs2[tt] = us[vs[j][1]]
            tt += 1
        i = i>>1
    if t != (N+1)//2:
        continue
    rs2.sort()
    for i in range(N//2):
        rs[i*2+1] = rs2[i]
    b,ff = 0,0
    for z,j in rs:
        if b>z:
            ff = 1
            break
        b = z
    if ff:
        continue
#    print(rs)
    rs = [j+1 for _,j in rs]
    r = min(r, tento(rs))
print(r if r != 10**18 else -1)
