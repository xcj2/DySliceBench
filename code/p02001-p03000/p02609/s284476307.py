"""
NTC here
"""


#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase

profile = 0
pypy = 1


def iin(): return int(input())


def lin(): return list(map(int, input().split()))



def main():
    T = 1
    while T:
        T -= 1
        n = iin()
        a = list(map(int, list(input())))
        ans = []
        def calc(a, md):
            ch = len(a)-1
            rm = 0
            for i in a:
                if i:
                    rm = (rm+ pow(2, ch, md))%md
                ch -= 1
            return rm%md
        
        def bin_calc(a):
            ans = []
            while a:
                ans.append(a&1)
                a >>= 1
            return ans[::-1]
        sm = sum(a)
        dc = {}
        if sm:
            dc[sm] = calc(a, sm)
        if sm-1>0:
            dc[sm-1] = calc(a, sm-1)
        dc[sm+1] = calc(a, sm+1)
        # count = 0
        for i in range(n):
            sol = 0
            s1 = sm - a[i]
            a[i] = + (not a[i])
            s1 += a[i]
            if s1:
                r1 = dc[s1]
                if a[i]:
                    r1 = (r1 + pow(2, n-i-1, s1))%s1
                else:
                    r1 = (r1 - pow(2, n-i-1, s1))%s1
                sol += 1
                a1 = bin_calc(r1)
                s1 = sum(a1)
                while s1:
                    # count += 1
                    # print(a1, s1)
                    sol += 1
                    rm = calc(a1, s1)
                    
                    if rm:
                        a1 = bin_calc(rm)
                        s1 = sum(a1)
                    else:
                        break
            a[i] = + (not a[i])
            ans.append(sol)
        print(*ans, sep='\n')





    
        










    




                

        

 
 
 
 
 
 
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
 
if pypy:
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
    input = lambda: sys.stdin.readline().rstrip("\r\n")
 
# endregion
 
if __name__ == "__main__":
    if profile:
        import cProfile
        cProfile.run('main()')
    else:
        main()
