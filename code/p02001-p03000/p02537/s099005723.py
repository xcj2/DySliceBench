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
input = stdin.buffer.readline

def main():
    n, k = map(int, input().split())

    # その値で終わる最長部分列の長さを格納
    st = SegmentTree(n=300001, default=0)

    for _ in range(n):
        a = int(input())
        st.update(a, st.query(max(0, a - k), min(300001, a + k + 1)) + 1)

    print(st.data[1])

main()