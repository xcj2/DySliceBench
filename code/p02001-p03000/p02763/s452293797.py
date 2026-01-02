class SegmentTree:
    def __init__(self, initial_values, f=max, zero=0):
        self.__size = len(initial_values)
        self.__n = 1 << ((self.__size - 1).bit_length())
        self.__f = f
        self.__z = zero
        self.__dat = [zero for _ in range(2 * self.__n)]
        zi = self.__n - 1
        for i, v in enumerate(initial_values):
            self.__dat[zi + i] = v
        for i in range(zi-1, -1, -1):
            self.__dat[i] = self.__f(self.__dat[2*i+1], self.__dat[2*i+2])
    
    def update(self, index, value):
        i = self.__n + index - 1
        if self.__dat[i] == value: return
        self.__dat[i] = value
        while i > 0:
            i = (i-1)//2
            self.__dat[i] = self.__f(self.__dat[2*i+1], self.__dat[2*i+2])
    
    def query(self, from_inclusive, to_exclusive):
        if to_exclusive <= from_inclusive: return self.__z
        a, b = self.__n + from_inclusive - 1, self.__n + to_exclusive - 2
        ans = self.__z
        while b - a > 1:
            if a&1 == 0: ans = self.__f(ans, self.__dat[a])
            if b&1 == 1: ans, b = self.__f(ans, self.__dat[b]), b-1
            a, b = a//2, (b-1)//2
        ans = self.__f(ans, self.__dat[a])
        if a != b: ans = self.__f(ans, self.__dat[b])
        return ans

N = int(input())
S = input()
g = lambda c: 1 << (ord(c)-ord('a'))
tree = SegmentTree([g(c) for c in S], lambda x,y:x|y)
Q = int(input())
for _ in range(Q):
    t, a, b = input().split()
    if t == '1': tree.update(int(a)-1, g(b))
    else: print(bin(tree.query(int(a)-1, int(b))).count('1'))