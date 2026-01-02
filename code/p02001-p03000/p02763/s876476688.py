import sys
def main():
    input = sys.stdin.readline
    N = int(input())
    S = input().rstrip()
    S = [conv(c) for c in S]
    segtree = SegmentTree(initial_values=S, f=lambda x,y:x|y)

    Q = int(input())
    for _ in range(Q):
        t, a, b = input().rstrip().split()
        if t == '1':
            a = int(a) - 1
            segtree.set_val(a, conv(b))
        else:
            a, b = int(a) - 1, int(b)
            q = segtree.query(a, b)
            print(popcount(q))

def conv(c): return 1 << (ord(c) - ord('a'))
def popcount(x):
    x = (x & 0x5555555555555555) + (x >> 1 & 0x5555555555555555)
    x = (x & 0x3333333333333333) + (x >> 2 & 0x3333333333333333)
    x = x + (x >> 4) & 0x0f0f0f0f0f0f0f0f
    x += x >> 8
    x += x >> 16
    x += x >> 32
    return x & 0x7f

class SegmentTree:
    def __init__(self, n=None, f=max, identity_factory=int, initial_values=None):
        assert(n or initial_values)
        size = n if n else len(initial_values)
        d = [identity_factory() for _ in range(2 * size + 1)]
        self.__n, self.__d, self.__f, self.__e = size, d, f, identity_factory
        if initial_values:
            for i, v in enumerate(initial_values): d[size + i] = v
            for i in range(size - 1, 0, -1): d[i] = f(d[i<<1], d[i<<1|1])

    def get_val(self, index):
        return self.__d[index + self.__n]

    def set_val(self, index, value):
        i, d, f = index + self.__n, self.__d, self.__f
        if d[i] == value: return
        d[i] = value
        while i:
            i = i >> 1
            d[i] = f(d[i<<1], d[i<<1|1])

    def modify(self, index, value):
        self.set_val(index, self.__f(self.__d[index + self.__n], value))

    def query(self, from_inclusive, to_exclusive):
        ans = self.__e()
        if to_exclusive <= from_inclusive: return ans
        l, r, d, f = from_inclusive + self.__n, to_exclusive + self.__n, self.__d, self.__f
        while l < r:
            if l & 1: ans, l = f(ans, d[l]), l+1
            if r & 1: ans, r = f(d[r-1], ans), r-1
            l, r = l >> 1, r >> 1
        return ans

    def bisect_left(self, func):
        '''func()がFalseになるもっとも左のindexを探す
        '''
        i, n, f, d, v = 1, self.__n, self.__f, self.__d, self.__e()
        while i < n:
            if func(f(v, d[i<<1])): v, i = f(v, d[i<<1]), i<<1|1
            else: i = i<<1
        return i - n


if __name__ == '__main__':
    main()