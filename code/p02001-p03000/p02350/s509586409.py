class LazySegTree: # Non Recursion, RmQ, RUQ
    def __init__(self, N):
        self.N = N
        self._N = 1<<((N-1).bit_length())
        self.INF = (1<<31) - 1
        self.node = [self.INF]*2*self._N
        self.lazy = [None]*2*self._N

    def build(self, lis):
        for i in range(self.N):
            self.node[i+self._N-1] = lis[i]
        for i in range(self._N-2,-1,-1):
            self.node[i] = self.node[i*2+1] + self.node[i*2+2]

    def _gindex(self, l, r):
        left = l + self._N; right = r + self._N
        lm = (left // (left & -left)) >> 1
        rm = (right // (right & -right)) >> 1
        while left < right:
            if right <= rm: yield right
            if left <= lm: yield left
            left >>= 1; right >>= 1
        while left:
            yield left
            left >>= 1

    def propagates(self, *ids): # ids: 1-indexded
        for i in reversed(ids):
            v = self.lazy[i-1]
            if v is None: continue
            self.lazy[2*i-1] = self.node[2*i-1] = v
            self.lazy[2*i] = self.node[2*i] = v
            self.lazy[i-1] = None
        return

    def update(self, l, r, x): # change all[left, right) to x
        *ids, = self._gindex(l, r)
        self.propagates(*ids)
        left = l + self._N; right = r + self._N
        while left < right:
            if left & 1:
                self.lazy[left-1] = self.node[left-1] = x
                left += 1
            if right & 1:
                right -= 1
                self.lazy[right-1] = self.node[right-1] = x
            left >>= 1; right >>= 1
        for i in ids:
            self.node[i-1] = min(self.node[2*i-1], self.node[2*i])

    def query(self, l, r):
        self.propagates(*self._gindex(l, r))
        left = l + self._N; right = r + self._N
        ret = self.INF
        while left < right:
            if right & 1:
                right -= 1
                ret = min(ret, self.node[right-1])
            if left & 1:
                ret = min(ret, self.node[left-1])
                left += 1
            left >>= 1; right >>= 1
        return ret

nm = lambda: map(int, input().split())
n,q = nm()
S = LazySegTree(n)
for _ in range(q):
  v = list(nm())
  if v[0]:
    # print(S.node)
    # print(S.lazy)
    print(S.query(v[1], v[2]+1))
  else:
  	S.update(v[1], v[2]+1, v[3])
