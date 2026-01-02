
import sys
import math
import time
sys.setrecursionlimit(int(1e6))
if False:
    dprint = print
else:
    def dprint(*args):
        pass

class BIT:
    def __init__(self, n=0):
        self.n = n
        self.d = [0] * (n+1)
    
    def add(self, i, x=1):
        i = int(i+1) # index begin 1
        while i <= self.n:
            self.d[i] += x
            i += i&-i # add LSB
    
    def sum(self, i=None):
        x = 0
        i = int( i+1 if not (i is None) else self.n )
        while i > 0:
            x += self.d[i]
            i -= i&-i # sub LSB
        return x

n, q = list(map(int, input().split()))
c = list(map(int, input().split()))
dprint("n, q =", n, q)
dprint("c =", c)

# check colors pair index (s,t)
st = [0] * (n+1)
col_last = [0] * (n+1)
for i in range(n):
    t = i + 1
    col = c[i]
    s = col_last[col]
    if s > 0:
        st[s] = t
    col_last[col] = t
dprint("st =", st)

# input querys (l,r)
lr = [None] * n
qs = list()
sorted_qs = list()
for i in range(q):
    l, r = list(map(int, input().split()))
    qs.append((i,l,r)) 
sorted_qs = sorted(qs, key=lambda q: q[1], reverse=True)
dprint("qs =", qs)
dprint("sorted_qs =", sorted_qs)

i_qs = 0
x = n
d = BIT(n+1)
qs_ans = [0] * len(qs)
for i_qs in range(len(sorted_qs)):
    i, l, r = sorted_qs[i_qs]
    dprint("i, l, r", i, l, r)
    while (x >= l):
        if st[x] > 0:
            d.add(st[x])
            dprint("add x(s), t =", x, st[x])
        x -= 1
    qs_ans[i] = (r-l+1)-d.sum(r)

for ans in qs_ans:
    print(ans)
