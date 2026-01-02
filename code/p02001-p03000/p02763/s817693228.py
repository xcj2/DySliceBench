import sys
 
def main():
    input = sys.stdin.readline
    N = int(input())
    S = input().rstrip()
    tree = SegmentTree(initial_values=S, f=lambda x,y:x|y, converter=lambda c: 1 << (ord(c)-ord('a')))
    Q = int(input())
    update = tree.update
    query = tree.query
    for _ in range(Q):
        t, a, b = input().rstrip().split()
        if t == '1': update(int(a)-1, b)
        else: print(bin(query(int(a)-1, int(b))).count('1'))    

class SegmentTree:
    def __init__(self, n=None, f=max, zero_factory=int, converter=lambda x:x, initial_values=None):
        assert(n or initial_values)
        self.__f, self.__z, self.__c = f, zero_factory, converter
        size = n if n else len(initial_values)
        self.__n = 1 << ((size - 1).bit_length())
        d = [zero_factory() for _ in range(2 * self.__n + 1)]
        self.__dat = d
        if initial_values:
            for i, v in enumerate(initial_values): d[self.__n + i] = converter(v)
            for i in range(self.__n - 1, 0, -1): d[i] = f(d[i<<1], d[i<<1|1])

    def update(self, index, value):
        i, v, d, f = index + self.__n, self.__c(value), self.__dat, self.__f
        if d[i] == v: return
        d[i] = v
        while i:
            i = i >> 1
            d[i] = f(d[i<<1], d[i<<1|1])

    def query(self, from_inclusive, to_exclusive):
        ans = self.__z()
        if to_exclusive <= from_inclusive: return ans
        l, r, d, f = from_inclusive + self.__n, to_exclusive + self.__n, self.__dat, self.__f
        while l < r:
            if l & 1: ans, l = f(ans, d[l]), l+1
            if r & 1: ans, r = f(ans, d[r-1]), r-1
            l, r = l >> 1, r >> 1
        return ans

if __name__ == '__main__':
    main()
