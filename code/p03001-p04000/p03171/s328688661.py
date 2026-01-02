# ===============================================================================================
# importing some useful libraries.
from __future__ import division, print_function
from fractions import Fraction
import sys
import os
from io import BytesIO, IOBase

# If the element is already present in the list,

# the left most position where element has to be inserted is returned.
from bisect import bisect_right as br
from bisect import bisect

# If the element is already present in the list,
# the right most position where element has to be inserted is returned

# ==============================================================================================
# fast I/O region

BUFSIZE = 8192


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


from collections import defaultdict, deque


class Graph(object):
    def __init__(self, dic):
        self.dict = dic
        self.vertex = set()

    def addedge(self, a, b):
        if self.dict[a] == []:
            self.vertex.add(a)
        if b != None:
            self.dict[a].append(b)

    def con_com_util(self, i, unvisited, count, comp):
        for j in self.dict[i]:
            if j in unvisited:
                unvisited.remove(j)
                comp[count].append(j)
                comp = self.con_com_util(j, unvisited, count, comp)
        return comp

    def conn_components(self):
        unvisited = self.vertex.copy()
        count = 0
        comp = defaultdict(list)
        while unvisited:
            i = unvisited.pop()
            comp[count].append(i)
            comp = self.con_com_util(i, unvisited, count, comp)
            count += 1
        return (count, comp)


def countSetBits(n):
    count = 0
    while (n):
        n &= (n - 1)
        count += 1

    return count



from sys import setrecursionlimit
setrecursionlimit(1000000)

n=int(inp())
ar=lis()
dp=[[0 for _ in range(n+5) ] for i in range(n+5)]
for i in range(n):
    dp[i][i]=ar[i]






for i in range(n,-1,-1):
    for j in range(i+1,n):
        dp[i][j]=max(ar[i]-dp[i+1][j], ar[j]-dp[i][j-1])


print(dp[0][n-1])










