
MOD = 10 ** 9 + 7

def main():
    for _ in inputt(1):
        a, b, c, d = inputi()
        if ceil(c / b) <= ceil(a / d):
            print("Yes")
        else:
            print("No")


# region M


# region import
# 所有import部分

from math import *
from heapq import *
from itertools import *
from functools import reduce, lru_cache, partial
from collections import Counter, defaultdict
import re, copy, operator, cmath
import sys, io, os, builtins
sys.setrecursionlimit(1000)

# endregion

# region fastio

BUFSIZE = 8192
class FastIO(io.IOBase):
    newlines = 0
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = io.BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
class IOWrapper(io.IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
def print(*args, **kwargs):
    if args:
        sys.stdout.write(args[0])
        split = kwargs.pop("split", " ")
        for arg in args[1:]:
            sys.stdout.write(split)
            sys.stdout.write(arg)
    sys.stdout.write(kwargs.pop("end", "\n"))
def debug(*args, **kwargs):
    print("debug", *args, **kwargs)
    sys.stdout.flush()
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip()
inputt = lambda t = 0: range(t) if t else range(int(input()))
inputs = lambda: input().split()
inputi = lambda: map(int, inputs())
inputl = lambda t = 0, k = inputi: map(list, (k() for _ in range(t))) if t else list(k())

# endregion

# region bisect

def len(a):
    if isinstance(a, range):
        return -((a.start - a.stop) // a.step)
    return builtins.len(a)
def bisect_left(a, x, key = None, lo = 0, hi = None):
    if lo < 0: lo = 0
    if hi == None: hi = len(a)
    if key == None: key = do_nothing
    while lo < hi:
        mid = (lo + hi) // 2
        if key(a[mid]) < x: lo = mid + 1
        else: hi = mid
    return lo
def bisect_right(a, x, key = None, lo = 0, hi = None):
    if lo < 0: lo = 0
    if hi == None: hi = len(a)
    if key == None: key = do_nothing
    while lo < hi:
        mid = (lo + hi) // 2
        if x < key(a[mid]): hi = mid
        else: lo = mid + 1
    return lo
def insort_left(a, x, key = None, lo = 0, hi = None):
    lo = bisect_left(a, x, key, lo, hi)
    a.insert(lo, x)
def insort_right(a, x, key = None, lo = 0, hi = None):
    lo = bisect_right(a, x, key, lo, hi)
    a.insert(lo, x)
do_nothing = lambda x: x
bisect = bisect_right
insort = insort_right
def index(a, x, default = None, key = None, lo = 0, hi = None):
    if lo < 0: lo = 0
    if hi == None: hi = len(a)
    if key == None: key = do_nothing
    i = bisect_left(a, x, key, lo, hi)
    if lo <= i < hi and key(a[i]) == x: return a[i]
    if default != None: return default
    raise ValueError
def find_lt(a, x, default = None, key = None, lo = 0, hi = None):
    if lo < 0: lo = 0
    if hi == None: hi = len(a)
    i = bisect_left(a, x, key, lo, hi)
    if lo < i <= hi: return a[i - 1]
    if default != None: return default
    raise ValueError
def find_le(a, x, default = None, key = None, lo = 0, hi = None):
    if lo < 0: lo = 0
    if hi == None: hi = len(a)
    i = bisect_right(a, x, key, lo, hi)
    if lo < i <= hi: return a[i - 1]
    if default != None: return default
    raise ValueError
def find_gt(a, x, default = None, key = None, lo = 0, hi = None):
    if lo < 0: lo = 0
    if hi == None: hi = len(a)
    i = bisect_right(a, x, key, lo, hi)
    if lo <= i < hi: return a[i]
    if default != None: return default
    raise ValueError
def find_ge(a, x, default = None, key = None, lo = 0, hi = None):
    if lo < 0: lo = 0
    if hi == None: hi = len(a)
    i = bisect_left(a, x, key, lo, hi)
    if lo <= i < hi: return a[i]
    if default != None: return default
    raise ValueError

# endregion

# region csgraph
# TODO

class Tree:
    def __init__(n):
        self._n = n
        self._conn = [[] for _ in range(n)]
        self._list = [0] * n
    def connect(a, b):
        pass

# endregion

# region ntheory
# TODO

class Sieve:
    def __init__(self):
        self._n = 6
        self._list = [2, 3, 5, 7, 11, 13]
    def extend(self, n):
        pass


sieve = Sieve()
def isprime(n):
    pass
def prime(n):
    pass
def factorint(n):
    factordict = defaultdict(int)
    for i in sieve:
        if n <= i * i:
            break
        while not n % i:
            factordict[i] += 1
            n //= i
    if n != 1:
        factordict[n] += 1
    return factordict

# endregion

# region main

if __name__ == "__main__":
    main()

# endregion


# endregion