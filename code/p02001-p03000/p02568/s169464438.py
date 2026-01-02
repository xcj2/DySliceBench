import sys

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    MOD=998244353
    class Lazy_segtree:
    #遅延評価セグメント木
      def __init__(self, op, e, mapping, composition, id, v):
        if type(v) is int: v = [e()] * v
        self._n = len(v)
        self.log = self.ceil_pow2(self._n)
        self.size = 1 << self.log
        self.d = [e()] * (2 * self.size)
        self.lz = [id()] * self.size
        self.e = e
        self.op = op
        self.mapping = mapping
        self.composition = composition
        self.id = id
        for i in range(self._n): self.d[self.size + i] = v[i]
        for i in range(self.size - 1, 0, -1): self.update(i)

      # 1点更新
      def set(self, p, x):
        p += self.size
        for i in range(self.log, 0, -1): self.push(p >> i)
        self.d[p] = x
        for i in range(1, self.log + 1): self.update(p >> i)

      # 1点取得
      def get(self, p):
        p += self.size
        for i in range(self.log, 0, -1): self.push(p >> i)
        return self.d[p]

      # 区間演算
      def prod(self, l, r):
        if l == r: return self.e()
        l += self.size
        r += self.size
        for i in range(self.log, 0, -1):
          if (((l >> i) << i) != l): self.push(l >> i)
          if (((r >> i) << i) != r): self.push(r >> i)
        sml, smr = self.e(), self.e()
        while (l < r):
          if l & 1: 
            sml = self.op(sml, self.d[l])
            l += 1
          if r & 1:
            r -= 1
            smr = self.op(self.d[r], smr)
          l >>= 1
          r >>= 1
        return self.op(sml, smr)

      # 全体演算
      def all_prod(self): return self.d[1]

      # 1点写像
      def apply(self, p, f):
        p += self.size
        for i in range(self.log, 0, -1): self.push(p >> i)
        self.d[p] = self.mapping(f, self.d[p])
        for i in range(1, self.log + 1): self.update(p >> i)

      # 区間写像
      def apply(self, l, r, f):
        if l == r: return
        l += self.size
        r += self.size
        for i in range(self.log, 0, -1):
          if (((l >> i) << i) != l): self.push(l >> i)
          if (((r >> i) << i) != r): self.push((r - 1) >> i)
        l2, r2 = l, r
        while l < r:
          if l & 1: 
            sml = self.all_apply(l, f)
            l += 1
          if r & 1:
            r -= 1
            smr = self.all_apply(r, f)
          l >>= 1
          r >>= 1
        l, r = l2, r2
        for i in range(1, self.log + 1):
          if (((l >> i) << i) != l): self.update(l >> i)
          if (((r >> i) << i) != r): self.update((r - 1) >> i)

      # L固定時の最長区間のR
      def max_right(self, l, g):
        if l == self._n: return _n
        l += self.size
        for i in range(self.log, 0, -1): self.push(l >> i)
        sm = self.e()
        while True:
          while (l % 2 == 0): l >>= 1
          if not g(self.op(sm, self.d[l])):
            while l < self.size:
              self.push(l)
              l = 2 * l
              if g(self.op(sm, self.d[l])):
                sm = self.op(sm, self.d[l])
                l += 1
            return l - self.size
          sm = self.op(sm, self.d[l])
          l += 1
          if (l & -l) == l: break
        return self._n

      # R固定時の最長区間のL
      def min_left(self, r, g):
        if r == 0: return 0
        r += self.size
        for i in range(self.log, 0, -1): self.push((r - 1) >> i)
        sm = self.e()
        while True:
          r -= 1
          while r > 1 and (r % 2): r >>= 1
          if not g(self.op(self.d[r], sm)):
            while r < self.size:
              self.push(r)
              r = 2 * r + 1
              if g(self.op(self.d[r], sm)):
                sm = self.op(self.d[r], sm)
                r -= 1
            return r + 1 - self.size
          sm = self.op(self.d[r], sm)
          if (r & - r) == r: break
        return 0

      def update(self, k): self.d[k] = self.op(self.d[2 * k], self.d[2 * k + 1])
      
      def all_apply(self, k, f):
        self.d[k] = self.mapping(f, self.d[k])
        if k < self.size: self.lz[k] = self.composition(f, self.lz[k])
      
      def push(self, k):
        self.all_apply(2 * k, self.lz[k])
        self.all_apply(2 * k + 1, self.lz[k])
        self.lz[k] = self.id()
      
      def ceil_pow2(self, n):
        x = 0
        while (1 << x) < n: x += 1
        return x

    def e():
      return 0

    def op(s, t):
      sv, sn = s >> 32, s % (1 << 32)
      tv, tn = t >> 32, t % (1 << 32)
      return (((sv + tv) % MOD) << 32) + sn + tn

    def mapping(f, a):
      fb, fc = f >> 32, f % (1 << 32)
      av, an = a >> 32, a % (1 << 32)
      return (((fb * av + fc * an) % MOD) << 32) + an

    def composition(f, g):
      fb, fc = f >> 32, f % (1 << 32)
      gb, gc = g >> 32, g % (1 << 32)
      return ((fb * gb % MOD) << 32) + ((gc * fb + fc) % MOD)

    def id():
      return 1 << 32
  
    N,Q=MI()
    a=LI()
    for i in range(N):
        a[i]=(a[i]<<32) +1
    seg=Lazy_segtree(op,e,mapping,composition,id,a)
    for _ in range(Q):
        q=LI()
        if q[0]==0:
            _,l,r,b,c=q
            seg.apply(l,r,(b<<32)+c)
        else:
            _,l,r=q
            ans=seg.prod(l,r) >>32
            print(ans%MOD)
            
    
  
  

main()
