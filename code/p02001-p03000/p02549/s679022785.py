class segtree:
  #セグメント木
  def __init__(s, v, op, e):
    s._n = len(v)
    s.log = s.ceil_pow2(s._n)
    s.size = 1 << s.log
    s.d = [e()] * (2 * s.size)
    s.e = e
    s.op = op
    for i in range(s._n): s.d[s.size + i] = v[i]
    for i in range(s.size - 1, 0, -1): s.update(i)
  
  # 1点更新
  def set(s, p, x):
    p += s.size
    s.d[p] = x
    for i in range(1, s.log + 1): s.update(p >> i)
 
  # 1点取得
  def get(s, p):
    return s.d[p + s.size]
 
  # 区間演算
  def prod(s, l, r):
    sml, smr = s.e(), s.e()
    l += s.size
    r += s.size
    while (l < r):
      if l & 1: 
        sml = s.op(sml, s.d[l])
        l += 1
      if r & 1:
        r -= 1
        smr = s.op(s.d[r], smr)
      l >>= 1
      r >>= 1
    return s.op(sml, smr)
 
  # 全体演算
  def all_prod(s): return s.d[1]
 
  def update(s, k): s.d[k] = s.op(s.d[2 * k], s.d[2 * k + 1])
  def ceil_pow2(s, n):
    x = 0
    while (1 << x) < n: x += 1
    return x


N, K = list(map(int, input().split()))
LR = [list(map(int, input().split())) for _ in range(K)]
MOD = 998244353

def e():
  return 0
def op(a, b):
  return (a + b) % MOD

seg = segtree([0] * N, op, e)
seg.set(0, 1)

for i in range(1, N):
  ans = 0
  for l, r in LR:
    r, l = max(0, i - l + 1), max(0, i - r)
    ans = (ans + seg.prod(l, r)) % MOD
  seg.set(i, ans)

print(seg.get(N - 1))
