n, k = map(int,input().split())
lrl = []
for _ in range(k):
    lrl.append(list(map(int,input().split())))

N = 2 * n
# N: 処理する区間の長さ

data0 = [0]*(N+1)
data1 = [0]*(N+1)

mod = 998244353
# 区間[l, r)に x を加算
def _add(data, k, x):
    while k <= N:
        x %= mod
        data[k] += x
        data[k] %= mod
        k += k & -k
def add(l, r, x):
    _add(data0, l, -x*(l-1)%mod)
    _add(data0, r, x*(r-1)%mod)
    _add(data1, l, x)
    _add(data1, r, -x)

# 区間[l, r)の和を求める
def _get(data, k):
    s = 0
    while k:
        s += data[k]
        s %= mod
        k -= k & -k
    return s
def query(l, r):
    return _get(data1, r-1) * (r-1) + _get(data0, r-1) - _get(data1, l-1) * (l-1) - _get(data0, l-1)

add(1, 2, 1)
for i in range(n):
    now = query(i+1, i+2) 
    for l, r in lrl:
        add(l+i+1, r+i+2, now % mod)

print(query(n, n+1) % mod)
