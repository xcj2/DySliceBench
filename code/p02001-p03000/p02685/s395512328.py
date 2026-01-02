#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase


#a=[int(x) for x in input().split()]
#n=int(input())

def main():
    mod=998244353

    def po(a,n):
        ans=1
        while n:
            if n&1:
                ans=(ans*a)%mod
            a=(a*a)%mod
            n//=2
        return ans


    n,m,k=[int(x) for x in input().split()]
    
    f=[1]
    for i in range(1,n+5):
        f.append(f[-1]*i%mod)

    def fac(n):
        if n<0:
            return 0
        return f[n]
    
    def nCr(n,r):
        if n<0 or r>n or r<0:
            return 0
        return fac(n)*po(fac(r)*fac(n-r),mod-2)%mod

    val=0
    for i in range(k+1):
        ans=1
        ans=(ans*nCr(n-1,i))%mod
        ans=(ans*m)%mod
        ans=(ans*po(m-1,n-i-1))%mod
        val=(ans+val)%mod
    print(val)

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