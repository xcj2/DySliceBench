import sys
from bisect import bisect_left

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

class SegTree:
    def __init__(self, N, X_f, X_unit, X_commutative=False):
        self.N = N
        self.X_f = X_f
        self.X_unit = X_unit
        self.X = [self.X_unit] * (N + N)
        if X_commutative:
            self.fold = self._fold_commutative

    def build(self, seq):
        for i, x in enumerate(seq, self.N):
            self.X[i] = x
        for i in range(self.N - 1, 0, -1):
            self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])

    def set_val(self, i, x):
        i += self.N
        self.X[i] = x
        while i > 1:
            i >>= 1
            self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])

    def fold(self, L, R):
        L += self.N
        R += self.N
        vL = vR = self.X_unit
        while L < R:
            if L & 1:
                vL = self.X_f(vL, self.X[L])
                L += 1
            if R & 1:
                R -= 1
                vR = self.X_f(self.X[R], vR)
            L >>= 1
            R >>= 1
        return self.X_f(vL, vR)

    def _fold_commutative(self, L, R):
        L += self.N
        R += self.N
        v = self.X_unit
        while L < R:
            if L & 1:
                v = self.X_f(v, self.X[L])
                L += 1
            if R & 1:
                R -= 1
                v = self.X_f(v, self.X[R])
            L >>= 1
            R >>= 1
        return v

N = int(readline())
A = (0, ) + tuple(map(int, readline().split()))

m = map(int, read().split())
U, V = zip(*zip(m, m))

def edges_to_graphdata(A, B, N, M):
    head = [-1] * (N + 1)
    nxt = [0] * (M + M)
    to = [0] * (M + M)
    for i in range(M):
        a = A[i]
        b = B[i]
        nxt[i << 1] = head[a]
        to[i << 1] = b
        head[a] = i << 1
        nxt[i << 1 | 1] = head[b]
        to[i << 1 | 1] = a
        head[b] = i << 1 | 1
    return head, nxt, to

def EulerTour(head, nxt, to, root=1):
    N = len(head) - 1
    parent = [0] * (N + 1)
    ind_L = [0] * (N + 1)
    ind_R = [0] * (N + 1)
    i = -1
    tour = []
    stack = [-root, root]
    stack[0] = -root
    stack[1] = root
    while stack:
        v = stack.pop()
        tour.append(v)
        i += 1
        if v > 0:
            ind_L[v] = i
            p = parent[v]
            k = head[v]
            while k != -1:
                w = to[k]
                if w == p:
                    k = nxt[k]
                    continue
                parent[w] = v
                stack.append(-w)
                stack.append(w)
                k = nxt[k]
        else:
            ind_R[-v] = i
    return tour, ind_L, ind_R, parent

tour, ind_L, ind_R, parent = EulerTour(*edges_to_graphdata(U, V, N, N - 1))

depth = [0] * (N + 1)
d = 0
for e in tour:
    d += 1 if e > 0 else -1
    if e > 0:
        depth[e] = d

A = [x * (N + N + 10) - d for x, d in zip(A, depth)]
A_unique = sorted(A)
A_rank = [bisect_left(A_unique, x) for x in A]

seg = SegTree(N + 1, max, 0, X_commutative=True)
LIS = [0] * (N + 1)
for e in tour:
    if e > 0:
        i = A_rank[e]
        LIS[e] = seg.fold(0, i + 1) + 1
        seg.set_val(i, LIS[e])
    else:
        i = A_rank[-e]
        seg.set_val(i, 0)

for e in tour:
    if e > 0:
        LIS[e] = max(LIS[e], LIS[parent[e]])

print('\n'.join(map(str, LIS[1:])))