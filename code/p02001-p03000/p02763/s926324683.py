class SegmentTree:
    def __init__(self, initial_values, f=max, zero=0):
        self.__size = len(initial_values)
        self.__n = 1 << ((self.__size - 1).bit_length())
        self.__f = f
        self.__z = zero
        self.__dat = [zero] * (2 * self.__n)
        self.__get_leaf = lambda i: self.__n + i - 1
        self.__get_parent = lambda i: (i-1)//2
        self.__get_children = lambda i: (self.__dat[2*i+1], self.__dat[2*i+2])
        self.__is_left = lambda i: i&1 == 1
        self.__is_right = lambda i: i&1 == 0
        zi = self.__get_leaf(0)
        dat, get_children = self.__dat, self.__get_children
        for i, v in enumerate(initial_values):
            dat[zi + i] = v
        for i in range(zi-1, -1, -1):
            dat[i] = f(*get_children(i))
    
    def update(self, index, value):
        f, dat, get_leaf, get_parent, get_children = self.__f, self.__dat, self.__get_leaf, self.__get_parent, self.__get_children
        i = get_leaf(index)
        if dat[i] == value: return
        dat[i] = value
        while i > 0:
            i = get_parent(i)
            dat[i] = f(*get_children(i))
    
    def query(self, from_inclusive, to_exclusive):
        f, z, dat, get_leaf, get_parent, is_left, is_right = self.__f, self.__z, self.__dat, self.__get_leaf, self.__get_parent, self.__is_left, self.__is_right
        if to_exclusive <= from_inclusive: return z
        a, b = get_leaf(from_inclusive), get_leaf(to_exclusive) - 1
        ans = z
        while b - a > 1:
            if is_right(a): ans = f(ans, dat[a])
            if is_left(b): ans, b = f(ans, dat[b]), b-1
            a, b = a//2, get_parent(b)
        ans = f(ans, dat[a])
        if a != b: ans = f(ans, dat[b])
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