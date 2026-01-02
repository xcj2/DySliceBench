def main():
    import sys
    input = sys.stdin.readline

    n = int(input().rstrip('\n'))
    s = input().rstrip('\n')
    q = int(input().rstrip('\n'))
    Q = []

    for _ in range(q):
        Q.append(input().rstrip().split())

    class SegTree():
        def __init__(self, n_):
            self.n = 1
            while self.n < n_:
                self.n *= 2
            self.tree = []
            for _ in range(2 * self.n - 1):
                self.tree.append(2)
        def update(self, k, a):
            k += self.n - 1
            self.tree[k] = a
            while k > 0:
                k = (k - 1) // 2
                self.tree[k] = min(self.tree[k * 2 + 1], self.tree[k * 2 + 2])
        def query(self, l, r):
            l += self.n - 1
            r += self.n - 2
            res = 2
            while r-l>1:
                if l&1 == 0:
                    res = min(res,self.tree[l])
                if r&1 == 1:
                    res = min(res,self.tree[r])
                    r -= 1
                l = l//2
                r = (r-1)//2
            if l == r:
                res = min(res,self.tree[l])
            else:
                res = min(min(res,self.tree[l]),self.tree[r])
            return res

    d = { c: SegTree(n) for c in "abcdefghijklmnopqrstuvwxyz"}
    l = []

    for i, c in enumerate(s):
        d[c].update(i, 1)
        l.append(c)

    for a, b, c in Q:
        if a == "1":
            b = int(b) - 1
            d[l[b]].update(b, 2)
            d[c].update(b, 1)
            l[b] = c
        else:
            res = 0
            b, c = int(b), int(c)
            for key in d:
                if d[key].query(b-1, c) == 1:
                    res += 1
            print(res)


if __name__ == '__main__':
    main()
