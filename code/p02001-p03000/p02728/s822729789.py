#!/usr/bin/env python
from __future__ import division, print_function

import os
import sys
from io import BytesIO, IOBase

if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip


def main():
    n = int(input().strip())
    adj = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = [int(s) for s in input().strip().split()]
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)

    sys.setrecursionlimit(10 ** 6)
    
    M = 10 ** 9 + 7
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = (fact[i - 1] * i) % M
    
    def inv(x):
        return pow(x, M - 2, M)

    def comb(m, k):
        return (((fact[m] * inv(fact[k])) % M) * inv(fact[m - k])) % M

    result = [0] * n
    size = [1] * n
    low = [1] * n

    def dfs1(u, parent=-1):
        for v in adj[u]:
            if v == parent:
                continue
            dfs1(v, u)
            size[u] += size[v]
        remain = size[u] - 1
        for v in adj[u]:
            if v == parent:
                continue
            low[u] = (low[u] * comb(remain, size[v]) * low[v]) % M
            remain -= size[v]
    
    def dfs2(u, parent=-1, up=1):
        result[u] = (comb(n - 1, size[u] - 1) * low[u] * up) % M
        for v in adj[u]:
            if v == parent:
                continue
            dfs2(v, u, (result[u] * inv(comb(n - 1, size[v])) * inv(low[v])) % M)
    
    dfs1(0)
    # print(size)
    # print(low)
    dfs2(0)
    for x in result:
        print(x)


# region fastio

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

input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()
