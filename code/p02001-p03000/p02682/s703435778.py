
MOD = 10 ** 9 + 7
RLIMIT = 1000
DEBUG = 1

def main():
    for _ in inputt(1):
        a, b, c, k = inputi()
        t = k
        if k > a:
            t -= k - a
        if k > a + b:
            t -= k - a - b

        print(t)


# region M


# region import

from math import *
from heapq import *
from itertools import *
from functools import reduce, lru_cache, partial
from collections import Counter, defaultdict
import re, copy, operator, cmath
import sys, io, os, builtins
sys.setrecursionlimit(RLIMIT)

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
        sys.stdout.write(str(args[0]))
        split = kwargs.pop("split", " ")
        for arg in args[1:]:
            sys.stdout.write(split)
            sys.stdout.write(str(arg))
    sys.stdout.write(kwargs.pop("end", "\n"))
def debug(*args, **kwargs):
    if DEBUG and not __debug__:
        print("debug", *args, **kwargs)
        sys.stdout.flush()
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip()
inputt = lambda t = 0: range(t) if t else range(int(input()))
inputs = lambda: input().split()
inputi = lambda k = int: map(k, inputs())
inputl = lambda t = 0, k = lambda: list(inputi()): [k() for _ in range(t)] if t else list(k())

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

class Sieve:
    def __init__(self):
        self._n = 6
        self._list = [2, 3, 5, 7, 11, 13]
    def extend(self, n):
        if n <= self._list[-1]: return
        maxbase = int(n ** 0.5) + 1
        self.extend(maxbase)
        begin = self._list[-1] + 1
        newsieve = [i for i in range(begin, n + 1)]
        for p in self.primerange(2, maxbase):
            for i in range(-begin % p, len(newsieve), p):
                newsieve[i] = 0
        self._list.extend([x for x in newsieve if x])
    def extend_to_no(self, i):
        while len(self._list) < i: 
            self.extend(int(self._list[-1] * 1.5))
    def primerange(self, a, b):
        a = max(2, a)
        if a >= b: return
        self.extend(b)
        i = self.search(a)[1]
        maxi = len(self._list) + 1
        while i < maxi:
            p = self._list[i - 1]
            if p < b:
                yield p
                i += 1
            else: return
    def search(self, n):
        if n < 2: raise ValueError
        if n > self._list[-1]: self.extend(n)
        b = bisect(self._list, n)
        if self._list[b - 1] == n: return b, b
        else: return b, b + 1
    def __contains__(self, n):
        if n < 2: raise ValueError
        if not n % 2: return n == 2
        a, b = self.search(n)
        return a == b
    def __getitem__(self, n):
        if isinstance(n, slice):
            self.extend_to_no(n.stop + 1)
            return self._list[n.start: n.stop: n.step]
        else:
            self.extend_to_no(n + 1)
            return self._list[n]
sieve = Sieve()
def isprime(n):
    if n <= sieve._list[-1]:
        return n in sieve
    for i in sieve:
        if not n % i: return False
        if n < i * i: return True
prime = sieve.__getitem__
primerange = lambda a, b = 0: sieve.primerange(a, b) if b else sieve.primerange(2, a)
def factorint(n):
    factors = []
    for i in sieve:
        if n < i * i: break
        while not n % i:
            factors.append(i)
            n //= i
    if n != 1: factors.append(n)
    return factors
factordict = lambda n: Counter(factorint(n))

# endregion

# region main

if __name__ == "__main__":
    main()

# endregion


# endregion