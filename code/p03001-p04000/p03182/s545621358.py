N, M = map(int,input().split())
interval=[[] for i in range(N)]
for i in range(M):
    l, r, a = map(int,input().split())
    interval[r-1].append((l-1, a))

# N: 処理する区間の長さ
INF = 10**30-1

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
        data[i-1] = max(data[2*i-1], data[2*i])

# 区間[l, r)内の最大値を求める
def query(l, r):
    propagates(*gindex(l, r))
    L = N0 + l; R = N0 + r

    s = -INF
    while L < R:
        if R & 1:
            R -= 1
            s = max(s, data[R-1])
        if L & 1:
            s = max(s, data[L-1])
            L += 1
        L >>= 1; R >>= 1
    return s

dp=[0]*N # dp[i] = max upto i. SegTree maintans max s.t. rightmost 1 is at i

for i in range(N):
    for j in range(len(interval[i])):
        l, a = interval[i][j]
        update(l, i+1, a)
    dp[i] = max(query(0, i+1), 0)
    update(i+1, i+2, dp[i]) # write "max up to i" at i+1 so that, in the next step, updates yields "max s.t. rightmost 1 is at i+1"

print(dp[-1])