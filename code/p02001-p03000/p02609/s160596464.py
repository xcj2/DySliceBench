#!/usr/bin/env python3

'''
Author: andyli
Time: 2020-07-11 19:58:49
'''

import os
from io import BytesIO, IOBase
import sys


def main():
    n = int(input())
    x = input()
    popcounts = x.count('1')
    if popcounts == 1:
        for i in range(n):
            if x[i] == '1':
                print(0)
                continue
            if (i == n-1 and x[-1] == '0') or (i != n-1 and x[-1] == '1'):
                print(2)
            else:
                print(1)
        return
    if popcounts == 0:
        for i in range(n):
            print(1)
        
        return
    modmi = [0 for i in range(n+2)]
    modpl = [0 for i in range(n+2)]
    s = 1
    for i in range(0,n+2):
        s %= (popcounts-1)
        modmi[i] = s
        s <<= 1
    s = 1
    for i in range(0,n+2):
        s %= (popcounts+1)
        modpl[i] = s
        s <<= 1
    demodmi = int(x,base=2)%(popcounts-1)
    demodpl = int(x,base=2)%(popcounts+1)
    def count(n):
        ans = 0
        while n > 0:
            n %= bin(n).count('1')
            ans += 1
        return ans
    # print('\t',demodmi,demodpl)
    for i in range(n):
        if x[i] == '0':
            demodmi = (demodmi + modmi[(n-i-1)]) % (popcounts-1)
            demodpl = (demodpl + modpl[(n-i-1)]) % (popcounts+1)
            pass
        else:
            demodmi = (demodmi - modmi[(n-i-1)]) % (popcounts-1)
            demodpl = (demodpl - modpl[(n-i-1)]) % (popcounts+1)
            pass
        mod = demodmi if x[i] == '1' else demodpl
        # print('\t', mod)
        print(1 + count(mod))
        if x[i] == '1':
            demodmi = (demodmi + modmi[(n-i-1)]) % (popcounts-1)
            demodpl = (demodpl + modpl[(n-i-1)]) % (popcounts+1)
            pass
        else:
            demodmi = (demodmi - modmi[(n-i-1)]) % (popcounts-1)
            demodpl = (demodpl - modpl[(n-i-1)]) % (popcounts+1)
            pass

    return


# region fastio
BUFSIZE = 1048576


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = 'x' in file.mode or 'r' not in file.mode
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
            self.newlines = b.count(b'\n') + (not b)
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
        self.write = lambda s: self.buffer.write(s.encode('ascii'))
        self.read = lambda: self.buffer.read().decode('ascii')
        self.readline = lambda: self.buffer.readline().decode('ascii')


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
def input(): return sys.stdin.readline().rstrip('\r\n')

# endregion


if __name__ == '__main__':
    main()
