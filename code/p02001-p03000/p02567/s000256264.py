class SegmentTree():
    def __init__(self, arr, func=min, ie=2**63):
        self.h = (len(arr) - 1).bit_length()
        self.n = 2**self.h
        self.ie = ie
        self.func = func
        self.tree = [ie for _ in range(2 * self.n)]
        for i in range(len(arr)):
            self.tree[self.n + i] = arr[i]
        for i in range(1, self.n)[::-1]:
            self.tree[i] = func(self.tree[2 * i], self.tree[2 * i + 1])

    def set(self, idx, x):
        idx += self.n
        self.tree[idx] = x
        while idx:
            idx >>= 1
            self.tree[idx] = self.func(self.tree[2 * idx], self.tree[2 * idx + 1])

    def query(self, lt, rt):
        lt += self.n
        rt += self.n
        vl = vr = self.ie
        while rt - lt > 0:
            if lt & 1:
                vl = self.func(vl, self.tree[lt])
                lt += 1
            if rt & 1:
                rt -= 1
                vr = self.func(self.tree[rt], vr)
            lt >>= 1
            rt >>= 1
        return self.func(vl, vr)

import sys
input = sys.stdin.buffer.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))

st = SegmentTree(A, max, 0)
res = list()

for _ in range(Q):
    t, x, y = map(int, input().split())
    if t == 1:
        st.set(x - 1, y)
    elif t == 2:
        res.append(st.query(x - 1, y))
    else:
        hi = N + 1
        lo = x - 1
        while hi - lo > 1:
            mid = (hi + lo) // 2
            if st.query(x - 1, mid) >= y:
                hi = mid
            else:
                lo = mid
        res.append(lo + 1)

print('\n'.join(map(str, res)))