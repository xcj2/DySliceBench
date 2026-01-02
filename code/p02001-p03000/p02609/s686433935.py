#!/usr/bin/env python
#pyrival orz
import os
import sys
from io import BytesIO, IOBase

"""
    for _ in range(int(input())):
    n,m=map(int,input().split())
    n=int(input())
    a = [int(x) for x in input().split()]
"""

def main():
    from functools import lru_cache

    @lru_cache(None)
    def solve(n):
        if n==0:
            return 0
        c=bin(n).count('1')
        return 1+solve(n%c)
    n=int(input())
    s=input()

    ct=s.count('1')

    mod=1
    if ct>1:
        mod*=ct-1
    mod*=ct+1

    p,g=1,0
    for x in s:
        g*=2
        if x=='1':
            g+=1
        g%=mod

    s=s[::-1]
    ans=[0]*len(s)
    for i,x in enumerate(s):
        p%=mod
        if x=='1':
            if ct==1:
                p*=2
                continue
            else:
                ans[i]=1+solve((g-p)%(ct-1))
        else:
            ans[i]=1+solve((g+p)%(ct+1))
        p*=2
    ans=ans[::-1]
    for x in ans:
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


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()