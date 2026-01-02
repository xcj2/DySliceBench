import sys
input = sys.stdin.readline
N, Q = map(int, input().split())
mod = 998244353
class lazy_segtree:
  #遅延評価セグメント木
  def __init__(s, op, e, mapping, composition, id, v):
    if type(v) is int: v = [e()] * v
    s._n = len(v)
    s.log = s.ceil_pow2(s._n)
    s.size = 1 << s.log
    s.d = [e()] * (2 * s.size)
    s.lz = [id()] * s.size
    s.e = e
    s.op = op
    s.mapping = mapping
    s.composition = composition
    s.id = id
    for i in range(s._n): s.d[s.size + i] = v[i]
    for i in range(s.size - 1, 0, -1): s.update(i)
  
  # 1点更新
  def set(s, p, x):
    p += s.size
    for i in range(s.log, 0, -1): s.push(p >> i)
    s.d[p] = x
    for i in range(1, s.log + 1): s.update(p >> i)
 
  # 1点取得
  def get(s, p):
    p += s.size
    for i in range(s.log, 0, -1): s.push(p >> i)
    return s.d[p]
 
  # 区間演算
  def prod(s, l, r):
    if l == r: return s.e()
    l += s.size
    r += s.size
    for i in range(s.log, 0, -1):
      if (((l >> i) << i) != l): s.push(l >> i)
      if (((r >> i) << i) != r): s.push(r >> i)
    sml, smr = s.e(), s.e()
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
 
  # 1点写像
  def apply(s, p, f):
    p += s.size
    for i in range(s.log, 0, -1): s.push(p >> i)
    s.d[p] = s.mapping(f, s.d[p])
    for i in range(1, s.log + 1): s.update(p >> i)
 
  # 区間写像
  def apply(s, l, r, f):
    if l == r: return
    l += s.size
    r += s.size
    for i in range(s.log, 0, -1):
      if (((l >> i) << i) != l): s.push(l >> i)
      if (((r >> i) << i) != r): s.push((r - 1) >> i)
    l2, r2 = l, r
    while l < r:
      if l & 1: 
        sml = s.all_apply(l, f)
        l += 1
      if r & 1:
        r -= 1
        smr = s.all_apply(r, f)
      l >>= 1
      r >>= 1
    l, r = l2, r2
    for i in range(1, s.log + 1):
      if (((l >> i) << i) != l): s.update(l >> i)
      if (((r >> i) << i) != r): s.update((r - 1) >> i)
   
  # L固定時の最長区間のR
  def max_right(s, l, g):
    if l == s._n: return _n
    l += s.size
    for i in range(s.log, 0, -1): s.push(l >> i)
    sm = s.e()
    while True:
      while (l % 2 == 0): l >>= 1
      if not g(s.op(sm, s.d[l])):
        while l < s.size:
          s.push(l)
          l = 2 * l
          if g(s.op(sm, s.d[l])):
            sm = s.op(sm, s.d[l])
            l += 1
        return l - s.size
      sm = s.op(sm, s.d[l])
      l += 1
      if (l & -l) == l: break
    return s._n
 
  # R固定時の最長区間のL
  def min_left(s, r, g):
    if r == 0: return 0
    r += s.size
    for i in range(s.log, 0, -1): s.push((r - 1) >> i)
    sm = s.e()
    while True:
      r -= 1
      while r > 1 and (r % 2): r >>= 1
      if not g(s.op(s.d[r], sm)):
        while r < s.size:
          s.push(r)
          r = 2 * r + 1
          if g(s.op(s.d[r], sm)):
            sm = s.op(s.d[r], sm)
            r -= 1
        return r + 1 - s.size
      sm = s.op(s.d[r], sm)
      if (r & - r) == r: break
    return 0
 
  def update(s, k): s.d[k] = s.op(s.d[2 * k], s.d[2 * k + 1])
  def all_apply(s, k, f):
    s.d[k] = s.mapping(f, s.d[k])
    if k < s.size: s.lz[k] = s.composition(f, s.lz[k])
  def push(s, k):
    s.all_apply(2 * k, s.lz[k])
    s.all_apply(2 * k + 1, s.lz[k])
    s.lz[k] = s.id()
  def ceil_pow2(s, n):
    x = 0
    while (1 << x) < n: x += 1
    return x
 
inf = 10 ** 18
def e():
  return 0
 
def op(x, y):
  x0, x1 = x >> 32, x % (1 << 32)
  y0, y1 = y >> 32, y % (1 << 32)
  return (((x0 + y0) % mod) << 32) + (x1 + y1) % mod
 
def mapping(f, x):
  x0, x1 = x >> 32, x % (1 << 32)
  if f != inf: return ((f * x1 % mod) << 32) + x1
  else: return x
 
def composition(f, g):
  if f != inf: return f
  else: return g
 
def id(x = inf): return x

a = [pow(10, N - i - 1, mod) for i in range(N)]
seg = lazy_segtree(op, e, mapping, composition, id, [(x << 32) + x for x in a])

for _ in range(Q):
  l, r, d = map(int, input().split())
  l -= 1
  seg.apply(l, r, d)
  print(seg.all_prod() >> 32)