#    !/usr/bin/env python3
#    encoding: UTF-8
#    Modified: <22/Jun/2019 06:07:06 PM>


#    ✪ H4WK3yE乡
#    Mohd. Farhan Tahir
#    Indian Institute Of Information Technology (IIIT), Gwalior


import sys
import os
from io import IOBase, BytesIO


def main():
    n = int(input())
    arr = [0] * n
    ans = 'Yes'
    d = {}
    for i in range(n):
        arr[i] = get_array()
        if arr[i][0] > arr[i][1]:
            ans = 'No'
        if arr[i][1] not in d:
            d[arr[i][1]] = 0
        d[arr[i][1]] += arr[i][0]
    if ans == 'No':
        print(ans)
        return
    od = sorted(list(d.items()))
    d = []
    for i in od:
        d.append([i[0], i[1]])
    for i in range(1, len(d)):
        d[i][1] += d[i - 1][1]

    for i in d:
        if i[0] < i[1]:
            ans = 'No'
            break

    print(ans)


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
        self.seek((self.tell(), self.seek(0, 2), super(FastIO, self).write(s))[0])
        return s

    def read(self):
        while self._fill():
            pass
        return super(FastIO, self).read()

    def readline(self):
        while self.newlines == 0:
            s = self._fill()
            self.newlines = s.count(b"\n") + (not s)
        self.newlines -= 1
        return super(FastIO, self).readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.getvalue())
            self.truncate(0), self.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        py2 = round(0.5)
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        if py2 == 1:
            self.write = self.buffer.write
            self.read = self.buffer.read
            self.readline = self.buffer.readline
        else:
            self.write = lambda s: self.buffer.write(s.encode("ascii"))
            self.read = lambda: self.buffer.read().decode("ascii")
            self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)


def get_array(): return list(map(int, sys.stdin.readline().split()))


def get_ints(): return map(int, sys.stdin.readline().split())


def input(): return sys.stdin.readline().strip()


if __name__ == "__main__":
    main()
