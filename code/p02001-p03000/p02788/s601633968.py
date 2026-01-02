import bisect
import math

n, d, a = map(int, input().split())
xh = []

for _ in range(n):
    x, h = map(int, input().split())
    xh.append((x, h))
xh.sort(key=lambda x: x[0])
xs = [x[0] for x in xh]

ranges = []
for x in xs:
    ranges.append(bisect.bisect_right(xs, x + 2 * d))


# N: 処理する区間の長さ
N = n
INF = 2**31-1

LV = (N-1).bit_length()
N0 = 2**LV
data = [0]*(2*N0)
lazy = [0]*(2*N0)

def gindex(l, r):
    L = (l + N0) >> 1; R = (r + N0) >> 1
    lc = 0 if l & 1 else (L & -L).bit_length()
    rc = 0 if r & 1 else (R & -R).bit_length()
    for i in range(LV):
        if rc <= i:
            yield R
        if L < R and lc <= i:
            yield L
        L >>= 1; R >>= 1

# 遅延伝搬処理
def propagates(*ids):
    for i in reversed(ids):
        v = lazy[i-1]
        if not v:
            continue
        lazy[2*i-1] += v; lazy[2*i] += v
        data[2*i-1] += v; data[2*i] += v
        lazy[i-1] = 0

# 区間[l, r)にxを加算
def update(l, r, x):
    *ids, = gindex(l, r)
    propagates(*ids)

    L = N0 + l; R = N0 + r
    while L < R:
        if R & 1:
            R -= 1
            lazy[R-1] += x; data[R-1] += x
        if L & 1:
            lazy[L-1] += x; data[L-1] += x
            L += 1
        L >>= 1; R >>= 1
    for i in ids:
        data[i-1] = min(data[2*i-1], data[2*i])

# 区間[l, r)内の最小値を求める
def query(l, r):
    propagates(*gindex(l, r))
    L = N0 + l; R = N0 + r

    s = INF
    while L < R:
        if R & 1:
            R -= 1
            s = min(s, data[R-1])
        if L & 1:
            s = min(s, data[L-1])
            L += 1
        L >>= 1; R >>= 1
    return s


for i, (x, h) in enumerate(xh):
    update(i, i + 1, h)

ans = 0
for i in range(n):
    v = query(i, i + 1)
    if v > 0:
        t = math.ceil(v / a)
        ans += t
        update(i, ranges[i], -t * a)
print(ans)
