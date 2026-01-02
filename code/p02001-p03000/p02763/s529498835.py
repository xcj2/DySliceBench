import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def main():
    N,S,Q,*q = read().split()
    S = S.decode()
    tree = SegmentTree(initial_values=S, f=lambda x,y:x|y, converter=lambda c: 1 << (ord(c)-ord('a')))
    update = tree.update
    query = tree.query
    for t, a, b in zip(*[iter(q)]*3):
        if t == b'1': update(int(a)-1, b)
        else: print(bin(query(int(a)-1, int(b))).count('1'))

class SegmentTree:
    def __init__(self, n=None, f=max, zero_factory=int, converter=lambda x:x, initial_values=None):
        assert(n or initial_values)
        size = n if n else len(initial_values)
        self.__f, self.__z, self.__c = f, zero_factory, converter
        self.__n = 1 << ((size - 1).bit_length())
        self.__dat = [zero_factory() for _ in range(2 * self.__n)]
        if initial_values:
            zi = self.__get_leaf(0)
            for i, v in enumerate(initial_values): self.__dat[zi + i] = converter(v)
            for i in range(zi-1, -1, -1): self.__dat[i] = f(*self.__get_children(i))

    def update(self, index, value):
        i, v = self.__get_leaf(index), self.__c(value)
        if self.__dat[i] == v: return
        self.__dat[i] = v
        while i:
            i = self.__get_parent(i)
            self.__dat[i] = self.__f(*self.__get_children(i))

    def query(self, from_inclusive, to_exclusive):
        ans = self.__z()
        if to_exclusive <= from_inclusive: return ans
        l, r = self.__get_leaf(from_inclusive), self.__get_leaf(to_exclusive) - 1
        while r - l > 1:
            if self.__is_right(l): ans = self.__f(ans, self.__dat[l])
            if self.__is_left(r): ans, r = self.__f(ans, self.__dat[r]), r-1
            l, r = l//2, self.__get_parent(r)
        ans = self.__f(ans, self.__dat[l])
        if l != r: ans = self.__f(ans, self.__dat[r])
        return ans

    def __get_leaf(self, i): return self.__n + i - 1
    def __get_parent(self, i): return (i-1)//2
    def __get_children(self, i): return (self.__dat[2*i+1], self.__dat[2*i+2])
    def __is_left(self, i): return i&1 == 1
    def __is_right(self, i): return i&1 == 0

if __name__ == '__main__':
    main()
