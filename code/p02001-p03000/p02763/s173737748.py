# Reference: https://qiita.com/dn6049949/items/afa12d5d079f518de368

# self.data: 1-indexed
#    __1__
#  _2_   _3_
# 4   5 6   7

# f(f(a, b), c) == f(a, f(b, c))

class SegmentTree:
    # a = [default] * n
    # O(n)
    def __init__(self, n, f=max, default=-2**30):
        self.num_leaf = 2 ** (n-1).bit_length()
        self.data = [default] * (2*self.num_leaf)
        self.f = f

    # a[i] = x
    # O(log(n))
    def update(self, i, x):
        i += self.num_leaf
        self.data[i] = x
        i >>= 1
        while i > 0:
            self.data[i] = self.f(self.data[2*i], self.data[2*i+1])
            i >>= 1

    # return f(a[l:r])
    # O(log(n))
    def query(self, l, r):
        l += self.num_leaf
        r += self.num_leaf - 1
        lres, rres = self.data[0], self.data[0] # self.data[0] == default
        while l < r:
            if l & 1:
                lres = self.f(lres, self.data[l])
                l += 1
            if not r & 1:
                rres = self.f(self.data[r], rres)
                r -= 1
            l >>= 1
            r >>= 1
        if l == r:
            res = self.f(self.f(lres, self.data[l]), rres)
        else:
            res = self.f(lres, rres)
        return res

    # You can use min_index only if f == max.
    # return min({i | x <= i and v <= a[i]}, self.num_leaf)
    # O(log(n))
    def min_index(self, x, v):
        x += self.num_leaf
        while self.data[x] < v:
            if x & 1:
                if x.bit_length() == (x+1).bit_length():
                    x += 1
                else:
                    return self.num_leaf
            else:
                x >>= 1
        while x < self.num_leaf:
            if self.data[2*x] >= v:
                x = 2*x
            else:
                x = 2*x + 1
        return x - self.num_leaf

from sys import stdin
def input():
    return stdin.readline().strip()

def main():
    n = int(input())
    s = list(input())

    forest = [SegmentTree(n, f=max, default=0) for _ in range(26)]
    for ind, si in enumerate(s):
        forest[ord(si) - 97].update(ind, 1)

    q = int(input())
    ans = []
    for _ in range(q):
        typ, l, r = input().split()
        l = int(l) - 1

        if typ == '1':
            forest[ord(s[l]) - 97].update(l, 0)
            s[l] = r
            forest[ord(r) - 97].update(l, 1)

        else:
            cnt = 0
            for tree in forest:
                if tree.min_index(l, 1) < int(r):
                    cnt += 1
            ans.append(cnt)

    for i in ans:
        print(i)

main()