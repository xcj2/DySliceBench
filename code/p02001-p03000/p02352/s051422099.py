import sys
input = sys.stdin.readline

class LazyPropSegmentTree:
    def __init__(self, lst, op, apply, comp, e, identity):
        self.n = len(lst)
        self.depth = (self.n - 1).bit_length()
        self.N = 1 << self.depth
        self.op = op # binary operation of elements
        self.apply = apply # function to apply to an element
        self.comp = comp # composition of functions
        self.e = e # identity element w.r.t. op
        self.identity = identity # identity element w.r.t. comp
        self.v, self.length = self._build(lst) # self.v is set to be 1-indexed for simplicity
        self.lazy = [self.identity] * (2 * self.N)
    
    def __getitem__(self, i):
        return self.fold(i, i+1)
    
    def _build(self, lst):
        # construction of a tree
        # total 2 * self.N elements (tree[0] is not used)
        e, N, op = self.e, self.N, self.op
        tree = [e] * N + lst + [e] * (N - self.n)
        length = [1] * (2 * N)
        for i in range(N - 1, 0, -1):
            lc, rc = i << 1, (i << 1)|1
            tree[i] = op(tree[lc], tree[rc])
            length[i] = length[lc] + length[rc]
        return tree, length
    
    def _indices(self, l, r):
        left = l + self.N; right = r + self.N
        left //= (left & (-left)); right //= (right & (-right))
        left >>= 1; right >>= 1
        while left != right:
            if left > right: yield left; left >>= 1
            else: yield right; right >>= 1
        while left > 0: yield left; left >>= 1
    
    # propagate self.lazy and self.v in a top-down manner
    def _propagate_topdown(self, *indices):
        identity, v, lazy, length, apply, comp = self.identity, self.v, self.lazy, self.length, self.apply, self.comp
        for k in reversed(indices):
            x = lazy[k]
            if x == identity: continue
            lc, rc = k << 1, (k << 1) | 1
            v[lc] = apply(v[lc], x, length[lc])
            lazy[lc] = comp(lazy[lc], x)
            v[rc] = apply(v[rc], x, length[rc])
            lazy[rc] = comp(lazy[rc], x)
            lazy[k] = identity # propagated

    # propagate self.v in a bottom-up manner
    def _propagate_bottomup(self, indices):
        v, op = self.v, self.op
        for k in indices: v[k] = op(v[k << 1], v[(k << 1)|1])

    # update for the query interval [l, r) with function x
    def update(self, l, r, x):
        *indices, = self._indices(l, r)
        self._propagate_topdown(*indices)

        N, v, lazy, length, apply, comp = self.N, self.v, self.lazy, self.length, self.apply, self.comp
        
        # update self.v and self.lazy for the query interval [l, r)
        left = l + N; right = r + N
        if left & 1: v[left] = apply(v[left], x, length[left]); left += 1
        if right & 1: right -= 1; v[right] = apply(v[right], x, length[right])
        left >>= 1; right >>= 1
        while left < right:
            if left & 1:
                v[left] = apply(v[left], x, length[left])
                lazy[left] = comp(lazy[left], x)
                left += 1
            if right & 1:
                right -= 1
                v[right] = apply(v[right], x, length[right])
                lazy[right] = comp(lazy[right], x)
            left >>= 1; right >>= 1
        self._propagate_bottomup(indices)
    
    # returns answer for the query interval [l, r)
    def fold(self, l, r):
        self._propagate_topdown(*self._indices(l, r))
        
        e, N, v, op = self.e, self.N, self.v, self.op
        
        # calculate the answer for the query interval [l, r)
        left = l + N; right = r + N
        L = R = e
        while left < right:
            if left & 1: # self.v[left] is the right child
                L = op(L, v[left])
                left += 1
            if right & 1: # self.v[right-1] is the left child
                right -= 1
                R = op(v[right], R)
            left >>= 1; right >>= 1
        return op(L, R)
    
N, Q = map(int, input().split())
op = min
apply = lambda x, f, l: x + f
comp = lambda f, g: f + g
e = 2**31 - 1
identity = 0
A = [0] * N
lpsg = LazyPropSegmentTree(A, op, apply, comp, e, identity)
ans = []
for _ in range(Q):
    t, *arg, = map(int, input().split())
    if t == 0:
        s, t, x = arg
        lpsg.update(s, t+1, x)
    else:
        s, t = arg
        ans.append(lpsg.fold(s, t+1))
print('\n'.join(map(str, ans)))
