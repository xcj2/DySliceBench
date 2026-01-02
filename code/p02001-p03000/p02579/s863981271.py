#-------------------- fast io --------------------
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
        j = pi[j - 1]
        while j and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] =  j
    return pi

def prod(a):
    ans = 1
    for each in a:
        ans = (ans * each)
    return ans

def lcm(a, b): return a * b // gcd(a, b)

def binary(x, length=16):
    y = bin(x)[2:]
    return y if len(y) >= length else '0' * (length - len(y)) + y



h, w = map(int, input().split())
ch, cw = map(int, input().split())
dh, dw = map(int, input().split())

board = []
for i in range(h):
    board += [input()]

from collections import deque
q = deque()
q.append((ch - 1, cw - 1))
ds = [1e9] * (h * w)
ds[(ch - 1) * w + cw - 1] = 0
di = ((1, 0), (0, 1), (-1, 0), (0, -1))
while q:
    r, c = q.popleft()
    for k in di:
        nr, nc = r + k[0], c + k[1]
        if 0 <= nr < h and 0 <= nc < w and board[nr][nc] == '.' and ds[nr * w + nc] > ds[r * w + c]:
            ds[nr * w + nc] = ds[r * w + c]
            q.appendleft((nr, nc))
    for nr in range(r - 2, r + 3):
        for nc in range(c - 2, c + 3):
            if 0 <= nr < h and 0 <= nc < w and board[nr][nc] == '.' and ds[nr * w + nc] > ds[r * w + c] + 1:
                ds[nr * w + nc] = ds[r * w + c] + 1
                q.append((nr, nc))

if ds[(dh - 1) * w + dw - 1] > 1e8:
    print(-1)
else:
    print(ds[(dh - 1) * w + dw - 1])
