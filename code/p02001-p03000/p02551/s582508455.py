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

import sys
    
def e():
  return N - 1

def op(s, t):
  return min(s, t)

def mapping(f, a):
  return min(f, a)

def composition(f, g):
  return min(f, g)

def id():
  return N - 1

N, Q = list(map(int, input().split()))
Query = [list(map(int, input().split())) for _ in range(Q)]

v = [N - 2] * ((N - 2) * 2)


ans = (N - 2) * (N - 2)
seg = lazy_segtree(op, e, mapping, composition, id, v)

for q, x in Query:
  x -= 2
  l = 0
  r = 0
  t = 0
  if q == 1:
    t = N - 2
  if q == 2:
    l += N - 2
    r += N - 2
  g = seg.get(x + t)
  ans -= g
  r += g
  seg.apply(l, r, x)

print(ans)