N,d,a = map(int,input().split())

# N: 処理する区間の長さ

data0 = [0]*(N+1)
data1 = [0]*(N+1)
# 区間[l, r)に x を加算
def _add(data, k, x):
    while k <= N:
        data[k] += x
        k += k & -k
def add(l, r, x):
    _add(data0, l, -x*(l-1))
    _add(data0, r, x*(r-1))
    _add(data1, l, x)
    _add(data1, r, -x)

# 区間[l, r)の和を求める
def _get(data, k):
    s = 0
    while k:
        s += data[k]
        k -= k & -k
    return s
def query(l, r):
    return _get(data1, r-1) * (r-1) + _get(data0, r-1) - _get(data1, l-1) * (l-1) - _get(data0, l-1)

xhl = []
for _ in range(N):
    x,h = map(int,input().split())
    xhl.append((x,h))

xhl = sorted(xhl)
xl = [x for x,h in xhl]

for idx in range(N):
    add(idx+1, idx+2, xhl[idx][1])

def ceil(a, b):
   return a // b + (a % b > 0)

import bisect

ans = 0
for i in range(N):
    hp = query(i + 1, i + 2)
    if hp > 0:
        count = ceil(hp, a)
        ans += count
        damage = count * a
        idx = bisect.bisect_right(xl, xl[i] + 2*d)
        add(i+1, idx+1, -damage)
print(ans)





