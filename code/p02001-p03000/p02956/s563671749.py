# Enclosed Points
import bisect
from collections import defaultdict


class SegTree():
    # 1-indexed
    def __init__(self, N, function, basement):
        self.n = N
        self.K = (self.n-1).bit_length()
        self.f = function
        self.b = basement
        self.seg = [basement]*(2**(self.K+1)+1)
        X = 2**self.K

    def update(self, k, value):
        X = 2**self.K
        k += X
        self.seg[k] += value
        while k:
            k = k >> 1
            self.seg[k] = self.f(self.seg[k << 1], self.seg[(k << 1) | 1])

    def query(self, L, R):
        num = 2**self.K
        L += num
        R += num
        vL = self.b
        vR = self.b
        while L < R:
            if L & 1:
                vL = self.f(vL, self.seg[L])
                L += 1
            if R & 1:
                R -= 1
                vR = self.f(self.seg[R], vR)
            L >>= 1
            R >>= 1
        return self.f(vL, vR)


def aggfunc(x, y):
    return x+y


def Press(lists):
    lists.sort()
    d = defaultdict(int)
    now = -float("inf")
    index = 0
    for i in range(len(lists)):
        if lists[i] > now:
            index += 1
            d[lists[i]] = index
            now = lists[i]
        elif lists[i] == now:
            d[lists[i]] = index
    return d


mod = 998244353
N = int(input())
Point = []
for i in range(N):
    x, y = map(int, input().split())
    Point.append((x, y, i))


def modifie():
    Point.sort(key=lambda x: (x[1], x[0]))
    X = []
    for x, y, i in Point:
        X.append(x)
    modified_point_x = Press(X)
    return modified_point_x


modified_point_x = modifie()
segtree = SegTree(N+1, aggfunc, 0)
below_below = defaultdict(int)

for i in range(N):
    x, y, index = Point[i]
    segtree.update(modified_point_x[x], 1)
    below_below[Point[i]] = segtree.query(0, modified_point_x[x]+1)

X, Y = [], []
for x, y, index in Point:
    X.append(x)
    Y.append(y)
X.sort()
Y.sort()

ans = 0
powers = [1 for i in range(3*10**5)]
for i in range(1, 3*10**5):
    powers[i] = powers[i-1]*2 % mod


def pows(K):
    return powers[K]


for i in range(N):
    x, y, index = Point[i]
    ZZ = below_below[Point[i]]-1
    XX = bisect.bisect_right(X, x)-ZZ-1
    WW = bisect.bisect_right(Y, y)-ZZ-1
    YY = N-1-XX-ZZ-WW
    ss = pow(2, N, mod)-1-pows(XX)-pows(YY)-pows(ZZ)-pows(WW)+4-(pows(XX)-1)*(pows(YY)-1) - \
        (pows(YY)-1)*(pows(WW)-1)-(pows(ZZ)-1) * \
        (pows(WW)-1)-(pows(ZZ)-1)*(pows(XX)-1)
    ans += ss
print(ans % mod)