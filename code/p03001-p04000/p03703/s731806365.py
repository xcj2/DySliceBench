
#セグ木
from collections import deque
def f(L, R): return L + R #マージ
def g(old, new): return old+new #更新
zero = 0 #マージにおける零元

class segtree:
    def __init__(self, N, z): #要素数、零元
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

#Verify https://atcoder.jp/contests/abc157/submissions/11965304

def zaatu(LIST):
    s = set(LIST)
    ar = list(s)
    ar.sort()
    dic = dict()
    for i in range(len(ar)): dic[ar[i]] = i
    return dic

n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
for i in range(n):
    a[i] -= k
    if i!=0: a[i] += a[i-1]
dic = zaatu(a)
seg = segtree(n+1, 0)
ans = 0
for num in a: ans += (num>=0)
for i in range(n): a[i] = dic[a[i]]
for i in range(n):
    ans += seg.query(0, a[i]+1)
    seg.update(1, a[i])
print(ans)
