N, K = map(int, input().split())
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
        s %= MOD
        k -= k & -k
    return s
def query(l, r):
    return _get(data1, r-1) * (r-1) + _get(data0, r-1) - _get(data1, l-1) * (l-1) - _get(data0, l-1)

MOD = 998244353


lr = [list(map(int, input().split())) for _ in range(K)]

dp = [0] * (N+10)
add(1, 2, 1)
for i in range(1, N+1):
    dp[i] = query(i, i+1) % MOD
    for l, r in lr:
        if i+l > N+1: continue
        add(l+i, min(i+r+1, N+1), dp[i])
    

print(dp[N])
