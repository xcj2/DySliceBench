import os
import sys
from io import BytesIO, IOBase
# from collections import defaultdict as dd
# from collections import deque as dq
# import itertools as it
# from math import sqrt, log, log2
# from fractions import Fraction

def main():
    t = 1
    for _ in range(t):
        # n = int(input)
        r, g, b = map(int, input().split())
        k = int(input())
        #nums = list(map(int, input().split()))
        while g <= r and k:
            g <<= 1
            k -= 1
        while b <= g and k:
            b <<= 1
            k -= 1
        
        if k == 0 and (b<=r or g<=r or b<=g):
            print('No')
        else:
            print('Yes')
            
        # b>g>r
        # if b>g>r:
        #     print('Yes')
        # else:
        # elif g>r:
        #     while b <= g and k:
        #         b <<= 1
        #         k -= 1
            
        #     if k == 0 and b<= g:
        #         print('No')
        #     else:
        #         print('Yes')

        # elif b > r:
        #     while g <= r and k:
        #         g <<= 1
        #         k -= 1
            
        #     if k == 0 and g<= r:
        #         print('No')
        #     elif g >= b:
        #         print('No')
        #     else:
        #         print('Yes')
        
        # else:





        




































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