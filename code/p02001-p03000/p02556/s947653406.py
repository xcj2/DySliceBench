#from bisect import bisect_left as bl                #c++ lowerbound bl(array,element)
#from bisect import bisect_right as br               #c++ upperbound br(array,element)
#from __future__ import print_function, division    #while using python2
# from itertools import accumulate
# from collections import defaultdict, Counter

def modinv(n,p):
    return pow(n,p-2,p)

def main():
    #sys.stdin = open('input.txt', 'r')
    #sys.stdout = open('output.txt', 'w')

    n = int(input())
    coords = []
    for i in range(n):
        coords.append([int(x) for x in input().split()])
    
    r = int(1e9)
    x1, y1 = [0, 0]
    x2, y2 = [r, 0]
    x3, y3 = [0, r]
    x4, y4 = [r, r]

    d1 = []
    d2 = []
    d3 = []
    d4 = []
    
    for x, y in coords:
        d1.append(abs(x-x1) + abs(y - y1))
        d2.append(abs(x-x2) + abs(y - y2))
        d3.append(abs(x-x3) + abs(y - y3))
        d4.append(abs(x-x4) + abs(y - y4))

    d1.sort()
    d2.sort()
    d3.sort()
    d4.sort()

    # print(*d1)
    # print(*d2)
    # print(*d3)
    # print(*d4)

    print(max(d1[-1] - d1[0], d2[-1] - d2[0], d3[-1] - d3[0], d4[-1] - d4[0]))


#------------------ Python 2 and 3 footer by Pajenegod and c1729-----------------------------------------
py2 = round(0.5)
if py2:
    from future_builtins import ascii, filter, hex, map, oct, zip
    range = xrange

import os, sys
from io import IOBase, BytesIO

BUFSIZE = 8192
class FastIO(BytesIO):
    newlines = 0
    def __init__(self, file):
        self._file = file
        self._fd = file.fileno()
        self.writable = "x" in file.mode or "w" in file.mode
        self.write = super(FastIO, self).write if self.writable else None

    def _fill(self):
        s = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
        self.seek((self.tell(), self.seek(0,2), super(FastIO, self).write(s))[0])
        return s
    def read(self):
        while self._fill(): pass
        return super(FastIO,self).read()

    def readline(self):
        while self.newlines == 0:
            s = self._fill(); self.newlines = s.count(b"\n") + (not s)
        self.newlines -= 1
        return super(FastIO, self).readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.getvalue())
            self.truncate(0), self.seek(0)

class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        if py2:
            self.write = self.buffer.write
            self.read = self.buffer.read
            self.readline = self.buffer.readline
        else:
            self.write = lambda s:self.buffer.write(s.encode('ascii'))
            self.read = lambda:self.buffer.read().decode('ascii')
            self.readline = lambda:self.buffer.readline().decode('ascii')

sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip('\r\n')

if __name__ == '__main__':
   main()
