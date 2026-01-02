# ------------------- fast io --------------------
import os
import sys
from io import BytesIO, IOBase

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


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# ------------------- fast io --------------------
from math import gcd, ceil


def pre(s):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi


def prod(a):
    ans = 1
    for each in a:
        ans = (ans * each)
    return ans


def lcm(a, b): return a * b // gcd(a, b)


def binary(x, length=16):
    y = bin(x)[2:]
    return y if len(y) >= length else "0" * (length - len(y)) + y


# Python3 code to find number of
# distinct numbers in a subarray
MAX = 1000001


# structure to store queries
class Query:
    def __init__(self, l, r, idx):
        self.l = l
        self.r = r
        self.idx = idx

    # updating the bit array


def update(idx, val, bit, n):
    while idx <= n:
        bit[idx] += val
        idx += idx & -idx

    # querying the bit array


def query(idx, bit, n):
    summ = 0
    while idx:
        summ += bit[idx]
        idx -= idx & -idx
    return summ


def answeringQueries(arr, n, queries, q):
    # initialising bit array
    bit = [0] * (n + 1)

    # holds the rightmost index of
    # any number as numbers of a[i]
    # are less than or equal to 10^6
    last_visit = [-1] * MAX

    # answer for each query
    ans = [0] * q

    query_counter = 0
    for i in range(n):

        # If last visit is not -1 update -1 at the
        # idx equal to last_visit[arr[i]]
        if last_visit[arr[i]] != -1:
            update(last_visit[arr[i]] + 1, -1, bit, n)

            # Setting last_visit[arr[i]] as i and
        # updating the bit array accordingly
        last_visit[arr[i]] = i
        update(i + 1, 1, bit, n)

        # If i is equal to r of any query store answer
        # for that query in ans[]
        while query_counter < q and queries[query_counter].r == i:
            ans[queries[query_counter].idx] = \
                query(queries[query_counter].r + 1, bit, n) - \
                query(queries[query_counter].l, bit, n)
            query_counter += 1

    # print answer for each query
    for i in range(q):
        print(ans[i])

    # Driver Code


n, q = map(int, input().split())
queries = []
a = list(map(int, input().split()))
for i in range(q):
    x, y = map(int, input().split())
    queries += [Query(x-1, y-1, i)]

queries.sort(key=lambda x: x.r)
answeringQueries(a, n, queries, q)