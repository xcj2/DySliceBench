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


for _ in range(int(input()) if not True else 1):
    n, k = map(int, input().split())
    #a, b = map(int, input().split())
    #c, d = map(int, input().split())
    a = list(map(int, input().split()))
    di = {}
    x = []
    for i in a:
        ab = abs(i)
        x += [ab]
        if ab not in di:
            di[ab] = []
        di[ab] += [1 if i>=0 else -1]

    x = sorted(x, reverse=True)
    signs = []
    for each in x:
        signs += [di[each].pop()]

    cursign = 1
    ans = 1
    firstpos = -1
    firstneg = 0
    nextpos = None
    nextneg = None
    for i in range(k):
        ans = (ans * x[i]) % (10**9+7)
        cursign *= signs[i]
        if signs[i] == 1:
            firstpos = i
        if signs[i] == -1:
            firstneg = i

    if cursign == 1:
        print(ans)
        quit()

    for i in range(k, len(x)):
        if signs[i] == 1 and nextpos is None:
            nextpos = i
        if signs[i] == -1 and nextneg is None:
            nextneg = i
    ansdex = [i for i in range(k)]
    from math import inf
    ans = ans*-1
    #print(ans)
    #print(nextpos)
    ans1, ans2 = -10**18, -10**18
    if nextpos is not None:
        ansd = [i for i in range(k)]
        ans22 = 1
        ansd[firstneg] = nextpos
        for each in ansd:
            ans22 = (ans22 * x[each]) % (10**9+7)
        ans2 = ans22

    if nextneg is not None and firstpos != -1:
        ansd = [i for i in range(k)]
        ans22 = 1
        ansd[firstpos] = nextneg
        for each in ansd:
            ans22 = (ans22 * x[each]) % (10 ** 9 + 7)
        ans1 = ans22
    if ans1 != -10**18 and ans2 != -10**18:
        print(ans1 if x[nextneg]/x[firstpos] > x[nextpos]/x[firstneg] else ans2 if x[nextneg]/x[firstpos] < x[nextpos]/x[firstneg] else max(ans1, ans2))
        quit()
    if ans1 != -10**18 or ans2 != -10**18:
        print(max(ans1, ans2))
        quit()

    a = sorted(a, reverse=True)
    ans=1
    for i in range(k):ans=(ans*(a[i])) % (10**9+7)
    print(ans)

