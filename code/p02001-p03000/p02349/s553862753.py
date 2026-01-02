from math import log2, ceil


class SegmentTree:
    def __init__(self, n):
        tn = 2 ** ceil(log2(n))
        self.a = [0] * (tn * 2)

    def find(self, c, l, r, i):
        if l == r:
            return self.a[c]
        mid = (l + r) // 2
        if i <= mid:
            return self.a[c] + self.find(c * 2, l, mid, i)
        else:
            return self.a[c] + self.find(c * 2 + 1, mid + 1, r, i)

    def add(self, c, l, r, s, t, x):
        if l == r or l == s and r == t:
            self.a[c] += x
            return
        mid = (l + r) // 2
        if t <= mid:
            self.add(c * 2, l, mid, s, t, x)
        elif s > mid:
            self.add(c * 2 + 1, mid + 1, r, s, t, x)
        else:
            self.add(c * 2, l, mid, s, mid, x)
            self.add(c * 2 + 1, mid + 1, r, mid + 1, t, x)


n, q = map(int, input().split())
st = SegmentTree(n)
for _ in range(q):
    query = input().split()
    if query[0] == '0':
        # CAUTION: DSL_2_D: i = 0,1,...,n-1.  DSL_2_E: i = 1,2,...,n.
        s, t, x = map(int, query[1:])
        st.add(1, 1, n, s, t, x)
    else:
        print(st.find(1, 1, n, int(query[1])))