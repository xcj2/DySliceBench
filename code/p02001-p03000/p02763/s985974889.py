

# ===============================================================================================
# importing some useful libraries.
from __future__ import division, print_function
from fractions import Fraction
import sys
import os
from io import BytesIO, IOBase
from itertools import *
import bisect
from heapq import *
from math import *
from copy import *
from collections import deque
from collections import Counter as counter  # Counter(list)  return a dict with {key: count}
from itertools import combinations as comb  # if a = [1,2,3] then print(list(comb(a,2))) -----> [(1, 2), (1, 3), (2, 3)]
from itertools import permutations as permutate
from bisect import bisect_left as bl
# If the element is already present in the list,

# the left most position where element has to be inserted is returned.
from bisect import bisect_right as br
from bisect import bisect

# If the element is already present in the list,
# the right most position where element has to be inserted is returned

# ==============================================================================================
# fast I/O region

BUFSIZE = 8192
from sys import stderr


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
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


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


def print(*args, **kwargs):
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop("sep", " "), kwargs.pop("file", sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        file.write(str(x))
        at_start = False
    file.write(kwargs.pop("end", "\n"))
    if kwargs.pop("flush", False):
        file.flush()


if sys.version_info[0] < 3:
    sys.stdin, sys.stdout = FastIO(sys.stdin), FastIO(sys.stdout)
else:
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)

# inp = lambda: sys.stdin.readline().rstrip("\r\n")

# ===============================================================================================
### START ITERATE RECURSION ###
from types import GeneratorType


def iterative(f, stack=[]):
    def wrapped_func(*args, **kwargs):
        if stack: return f(*args, **kwargs)
        to = f(*args, **kwargs)
        while True:
            if type(to) is GeneratorType:
                stack.append(to)
                to = next(to)
                continue
            stack.pop()
            if not stack: break
            to = stack[-1].send(to)
        return to

    return wrapped_func


#### END ITERATE RECURSION ####

# ===============================================================================================
# some shortcuts

mod = 1000000007


def inp(): return sys.stdin.readline().rstrip("\r\n")  # for fast input


def out(var): sys.stdout.write(str(var))  # for fast output, always take string


def lis(): return list(map(int, inp().split()))


def stringlis(): return list(map(str, inp().split()))


def sep(): return map(int, inp().split())


def strsep(): return map(str, inp().split())


def zerolist(n): return [0] * n


def nextline(): out("\n")  # as stdout.write always print sring.


def testcase(t):
    for p in range(t):
        solve()


def printlist(a):
    for p in range(0, len(a)):
        out(str(a[p]) + ' ')

def pow(x, y, p):
    res = 1  # Initialize result
    x = x % p  # Update x if it is more , than or equal to p
    if (x == 0):
        return 0
    while (y > 0):
        if ((y & 1) == 1):  # If y is odd, multiply, x with result
            res = (res * x) % p

        y = y >> 1  # y = y/2
        x = (x * x) % p
    return res

from functools import reduce

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def gcd(a, b):
    if a == b: return a
    while b > 0: a, b = b, a % b
    return a
# =========================================================================================

from operator import add
def solve():
    def sep():
        return map(int, input().strip().split(" "))

    def lis():
        return list(map(int, input().strip().split(" ")))
    class SegmentTree:
        def __init__(self, data, default=0, func=add):
            """initialize the segment tree with data"""
            self._default = default
            self._func = func
            self._len = len(data)
            self._size = _size = 1 << (self._len - 1).bit_length()

            self.data = [default] * (_size) + data + [default] * (_size - self._len)
            for i in range(_size - 1, -1, -1):
                self.data[i] = func(self.data[2 * i], self.data[2 * i + 1])

        def __delitem__(self, idx):
            self[idx] = self._default

        def __getitem__(self, idx):
            return self.data[idx + self._size]

        def __setitem__(self, idx, value):
            idx += self._size
            self.data[idx] = value
            idx >>= 1
            while idx:
                self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
                idx >>= 1


        def __len__(self):
            return self._len



        def query(self, start, stop):
            """func  of data[start, stop)"""
            start += self._size
            stop +=  self._size

            res_left = res_right = self._default
            while start < stop:
                if start & 1:
                    res_left = self._func(res_left, self.data[start])
                    start += 1
                if stop & 1:
                    stop -= 1
                    res_right = self._func(self.data[stop], res_right)
                start >>= 1
                stop >>= 1

            return self._func(res_left, res_right)


    def fun(i1,i2):
        s1=i1
        s2=i2
        k=s1.union(s2)
        return(k)

    n=int(input())
    ar=inp()
    temp=[]
    for i in range(n):
        t=set().copy()
        t.add(ar[i])
        temp.append(t)
    defa=(set().copy())
    seg=SegmentTree(temp,default=defa,func=fun)
    m=int(inp())
    for _ in range(m):
        # print(seg.data)
        a,b,c=(i for i in inp().strip().split(" "))
        if a=="2":
            b=int(b)
            c=int(c)
            print(len(seg.query(b-1,c)))
        else:
            b=int(b)
            t=set().copy()
            t.add(c)
            seg[b-1]=t.copy()













solve()
#testcase(int(inp()))

