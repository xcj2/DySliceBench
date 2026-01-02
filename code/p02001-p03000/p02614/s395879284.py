#from bisect import bisect_left as bl                #c++ lowerbound bl(array,element)
#from bisect import bisect_right as br               #c++ upperbound br(array,element)
#from __future__ import print_function, division    #while using python2


def modinv(n,p):
    return pow(n,p-2,p)

from itertools import combinations

def main():
    #sys.stdin = open('input.txt', 'r')
    #sys.stdout = open('output.txt', 'w')

    n, m, k = [int(x) for x in input().split()]
    mat = [[0] * m for i in range(n)]
    for i in range(n):
        s = input()
        for j in range(m):
            if s[j] == '.':
                mat[i][j] = 1
    # print(mat)

    c = 0
    rows = [x for x in range(n)]
    cols = [x for x in range(m)]

    new_rows = []
    new_cols = []

    # print(rows)
    # print(cols)

    for i in range(2, n+1):
        temp = list(combinations(rows, i))
        # print(temp)
        for x in temp:
            new_rows.append(list(x))
    rows = [[x] for x in range(n)]
    for x in new_rows:
        rows.append(x)

    for i in range(2, m+1):
        temp = list(combinations(cols, i))
        # print(temp)
        for x in temp:
            new_cols.append(list(x))
    cols = [[x] for x in range(m)]
    for x in new_cols:
        cols.append(x)

    rows.append([])
    cols.append([])
    # print(rows)
    # print(cols)
    

    ans = 0
    # print(mat)
    for r in range(len(rows)):
        for c in range(len(cols)):
            new_mat = [[0] * m for x in range(n)]
            
            row = rows[r]
            col = cols[c]
            
            for i in range(n):
                for j in range(m):
                    if i in row or j in col:
                        new_mat[i][j] = 2
                    else:
                        new_mat[i][j] = mat[i][j]
            

            count_black = 0
            # print(new_mat)
            for x in new_mat:
                count_black += x.count(0)
            if count_black == k:
                ans += 1
            # print(row, col)
            # print(new_mat)
            # print(ans)
            # print()
    print(ans)

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
