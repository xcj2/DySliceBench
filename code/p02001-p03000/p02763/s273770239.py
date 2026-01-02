class SegmentTree:
    def __init__(self, initial_values, f=max, zero=0):
        self.__size = len(initial_values)
        self.__n = 1 << ((self.__size - 1).bit_length())
        self.__f = f
        self.__z = zero
        self.__dat = [zero for _ in range(2 * self.__n)]
        self.__get_leaf = lambda i: self.__n + i - 1
        self.__get_parent = lambda i: (i-1)//2
        self.__get_children = lambda i: (self.__dat[2*i+1], self.__dat[2*i+2])
        self.__is_left = lambda i: i&1 == 1
        self.__is_right = lambda i: i&1 == 0
        zi = self.__get_leaf(0)
        for i, v in enumerate(initial_values):
            self.__dat[zi + i] = v
        for i in range(zi-1, -1, -1):
            self.__dat[i] = self.__f(*self.__get_children(i))
    
    def update(self, index, value):
        i = self.__get_leaf(index)
        if self.__dat[i] == value: return
        self.__dat[i] = value
        while i > 0:
            i = self.__get_parent(i)
            self.__dat[i] = self.__f(*self.__get_children(i))
    
    def query(self, from_inclusive, to_exclusive):
        if to_exclusive <= from_inclusive: return self.__z
        a, b = self.__get_leaf(from_inclusive), self.__get_leaf(to_exclusive) - 1
        ans = self.__z
        while b - a > 1:
            if self.__is_right(a): ans = self.__f(ans, self.__dat[a])
            if self.__is_left(b): ans, b = self.__f(ans, self.__dat[b]), b-1
            a, b = a//2, self.__get_parent(b)
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