#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase


def main():
    n,a,b,c=map(int,input().split())
    d={}
    d['A']=a
    d['B']=b
    d['C']=c

    ss=[input() for _ in range(n)]

    ans=[0]*n
    for i in range(n):
        s=ss[i]
        pos=0
        if d[s[0]]>d[s[1]]:
            pos=0
        elif d[s[1]]>d[s[0]] or i==n-1:
            pos=1
        elif s[0] in ss[i+1]:
            pos=1
        else:
            pos=0

        d[s[pos]]-=1
        d[s[pos^1]]+=1
        ans[i]=ord(s[pos^1])
    
        # print(d)

        if d['A']<0 or d['B']<0 or d['C']<0 :
            print("No")
            exit(0)
    print("Yes")
    print("\n".join(chr(x) for x in ans))

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