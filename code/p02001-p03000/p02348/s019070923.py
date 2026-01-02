from math import log2, ceil


class SegmentTree:
    def __init__(self, n):
        tn = 2 ** ceil(log2(n))
        self.a = [2 ** 31 - 1] * (tn * 2)

    def find(self, c, l, r, i):
        if self.a[c] != -1:
            return self.a[c]
        mid = (l + r) // 2
        if i <= mid:
            return self.find(c * 2, l, mid, i)
        else:
            return self.find(c * 2 + 1, mid + 1, r, i)

    def update(self, c, l, r, s, t, x):
        if l == s and r == t:
            self.a[c] = x
            return
        cv = self.a[c]
        if cv != -1:
            self.a[c * 2] = self.a[c * 2 + 1] = cv
            self.a[c] = -1
        mid = (l + r) // 2
        if t <= mid:
            self.update(c * 2, l, mid, s, t, x)
        elif s > mid:
            self.update(c * 2 + 1, mid + 1, r, s, t, x)
        else:
            self.update(c * 2, l, mid, s, mid, x)
            self.update(c * 2 + 1, mid + 1, r, mid + 1, t, x)


n, q = map(int, input().split())
st = SegmentTree(n)
for _ in range(q):
    query = input().split()
    if query[0] == '0':
        s, t, x = map(int, query[1:])
        st.update(1, 0, n - 1, s, t, x)
    else:
        print(st.find(1, 0, n - 1, int(query[1])))