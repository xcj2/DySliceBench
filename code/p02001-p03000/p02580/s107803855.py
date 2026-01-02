# by the authority of GOD    author: manhar singh sachdev #

import os,sys
from io import BytesIO, IOBase
from collections import Counter,defaultdict

def main():
    h,w,m = map(int,input().split())
    tar = [tuple(map(int,input().split())) for _ in range(m)]
    tar = set(tar)
    row,col = Counter(),Counter()
    for i in tar:
        row[i[0]] += 1
        col[i[1]] += 1
    row1,col1 = defaultdict(list),defaultdict(list)
    for i in row:
        row1[row[i]].append(i)
    for i in col:
        col1[col[i]].append(i)
    x = max(row1)
    y = max(col1)
    fl = 1
    for i in row1[x]:
        for j in col1[y]:
            if (i,j) not in tar:
                fl = 0
                break
    print(x+y-fl)

#Fast IO Region
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

if __name__ == '__main__':
    main()