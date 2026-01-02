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



def prod(a):
    ans = 1
    for each in a:
        ans = (ans * each)
    return ans

def lcm(a, b): return a * b // gcd(a, b)


def binary(x, length=16):
    y = bin(x)[2:]
    return y if len(y) >= length else "0" * (length - len(y)) + y
from math import inf

for _ in range(int(input()) if not True else 1):
    #n = int(input())
    n, k = map(int, input().split())
    #a, b = map(int, input().split())
    #c, d = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = -inf
    for i in range(n):
        st = set()
        st.add(i)
        cur = i
        x = []
        while p[cur]-1 not in st:
            cur = p[cur]-1
            st.add(cur)
            x += [c[cur]]
        x += [c[p[cur]-1]]

        pre = [0]*len(x)
        pre[0] = x[0]
        for i in range(1, len(x)):
            pre[i] = pre[i-1] + x[i]
        if len(x) >= k:
            ans = max(ans, max(pre[:k]))
        else:
            kc = k
            kcc = k
            anss = 0
            if pre[-1] > 0:
                anss += pre[-1]*(kc // len(x))
                kc = kc % len(x)
                if kc:
                    anss += max(pre[:kc])
                ans = max(ans, anss, max(pre)+(pre[-1]*((kcc // len(x))-1)))
            else:
                ans = max(ans, max(pre))
    print(ans)