#セグ木
from collections import deque
def f(L, R): return L|R # merge
def g(old, new): return old^new  # update
zero = 0 #零元

class segtree:
    def __init__(self, N, z):
        self.M = 1
        while self.M<N: self.M *= 2
        self.dat = [z] * (self.M*2-1)
        self.ZERO = z

    def update(self, x, idx, l=0, r=-1):
        if r==-1: r = self.M
        idx += self.M-1
        self.dat[idx] = g(self.dat[idx], x)
        while idx > 0:
            idx = (idx-1)//2
            self.dat[idx] = f(self.dat[idx*2+1], self.dat[idx*2+2])

    def query(self, a, b=-1, idx=0, l=0, r=-1):
        if r==-1: r = self.M
        if b==-1: b = self.M
        q = deque([])
        q.append([l, r, 0])
        ret = self.ZERO
        while len(q):
            tmp = q.popleft()
            L = tmp[0]
            R = tmp[1]
            if R<=a or b<=L: continue
            elif a<=L and R<=b:
                ret = f(ret, self.dat[tmp[2]])
            else:
                q.append([L, (L+R)//2, tmp[2]*2+1])
                q.append([(L+R)//2, R, tmp[2]*2+2])
        return ret
n = int(input())
s = list(input())
q = int(input())
seg = segtree(n+1, 0)

for i in range(n):
    num = ord(s[i]) - ord("a")
    seg.update((1<<num), i)
for _ in range(q):
    a, b, c = input().split()
    b = int(b) - 1
    if a == "1":
        pre = ord(s[b]) - ord("a")
        now = ord(c) - ord("a")
        seg.update((1<<pre), b)
        seg.update((1<<now), b)
        s[b] = c
    else:
        q = seg.query(b, int(c))
        bin(q).count("1")
        print(bin(q).count("1"))
