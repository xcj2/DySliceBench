# region fastio  # from https://codeforces.com/contest/1333/submission/75948789
import sys, io, os

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


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

def main():

    from bisect import bisect_left as bl, bisect_right as br, insort
    import sys
    import heapq
    # from math import *
    from collections import defaultdict as dd, deque
    def data():
        return sys.stdin.readline().strip()

    def mdata():
        return map(int, data().split())

    out = sys.stdout.write
    # sys.setrecursionlimit(100000)
    INF = int(10e9)

    def knapSack(V):
        for i in range(n + 1):
            for v in range(V + 1):
                if v == 0:
                    K[i][v] = 0
                elif val[i - 1] <= v:
                    K[i][v] = min(wt[i - 1] + K[i - 1][v - val[i - 1]], K[i - 1][v])
                else:
                    K[i][v] = K[i - 1][v]

        return K[n][V]

    n, w = mdata()
    val = [0] * (n)
    wt = [0] * (n)
    for i in range(n):
        wt[i], val[i] = mdata()
    V = 100005
    K = [[1000000007 for x in range(V + 1)] for x in range(n + 1)]
    knapSack(V)
    m = 0
    for i in range(n + 1):
        for v in range(V + 1):
            if 1 <= K[i][v] <= w:
                m = max(m, v)
    print(m)

if __name__ == '__main__':
    main()