import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,k = list(map(int, input().split()))
a = [int(input()) for _ in range(n)]
for i in range(n):
    a[i] -= k
def cumsum(a):
    """※ aを破壊する
    l[i] = sum(a[:i]) なるlを返す
    sum(a[i:j]) == l[j+1] - l[i]
    """
    c = 0
    n = len(a)
    a.insert(0, 0)
    for i in range(1, n+1):
        a[i] = a[i-1]+a[i]
    return a
cumsum(a)
l = [a[0]]
ans = 0
### BIT binary
def init(bit, values):
    for i,v in enumerate(values):
        add(bit,i+1,v)
#a1 ~ aiまでの和 O(logn)
def query(bit,i):
    res = 0
    while i > 0:
        res += bit[i]
        i -= i&(-i)
    return res

#ai += x(logN)
def add(bit,i,x):
    if i==0:
        raise RuntimeError
    while i <= len(bit)-1:
        bit[i] += x
        i += i&(-i)
    return

# a1,...,aiの和がv以上になる最小のindexを求める
def index(bit, v):
    i = 0
    k = 1
    n = len(bit)-1
    while 2*k<n:
        k *= 2
    while k>0:
        if i+k<n+1 and bit[i+k]<v:
            v -= bit[i+k]
            i += k
        k //= 2
    return i+1

from bisect import bisect_left
from bisect import bisect_left as bl, bisect_right as br

def press(l):
    # xs[inds[i]]==l[i]となる
    xs = sorted(set(l))
    inds = [None] * len(l)
    for i,item in enumerate(l):
        inds[i] = bisect_left(xs, item)
    return xs, inds
xs, inds = press(a)
bit = [0]*(len(inds)+1)
ans = 0
num = 0
for i in inds:
    ans += query(bit, i+1)
    add(bit, i+1, 1)
#     print(i, ii, xs[i])
    num += 1
print(ans)