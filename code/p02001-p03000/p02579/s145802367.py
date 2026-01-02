# by the authority of GOD    author: manhar singh sachdev #

import os,sys
from io import BytesIO, IOBase
from collections import deque,defaultdict

def main():
    h,w = map(int,input().split())
    x1,y1 = map(int,input().split())
    a1,b1 = map(int,input().split())
    arr = [list(input().strip()) for _ in range(h)]
    dp = [[0]*w for _ in range(h)]
    se = set()
    for i in range(h):
        for j in range(w):
            if arr[i][j] != '#':
                se.add((i,j))
    reg = 1
    while len(se):
        x = se.pop()
        curr = deque([x])
        while len(curr):
            y = curr.popleft()
            z = (y[0]+1,y[1])
            dp[y[0]][y[1]] = reg
            if z[0]<h and z[1]<w and z in se and arr[z[0]][z[1]] != '#':
                curr.append(z)
                se.remove(z)
                dp[z[0]][z[1]] = reg
            z = (y[0],y[1]+1)
            if z[0] < h and z[1] < w and z in se and arr[z[0]][z[1]] != '#':
                curr.append(z)
                se.remove(z)
                dp[z[0]][z[1]] = reg
            z = (y[0]-1, y[1])
            if z[0] >= 0 and z[1] >= 0 and z in se and arr[z[0]][z[1]] != '#':
                curr.append(z)
                se.remove(z)
                dp[z[0]][z[1]] = reg
            z = (y[0],y[1] - 1)
            if z[0] >= 0 and z[1] >= 0 and z in se and arr[z[0]][z[1]] != '#':
                curr.append(z)
                se.remove(z)
                dp[z[0]][z[1]] = reg
        reg += 1
    path = defaultdict(set)
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '#':
                continue
            for r in range(-2,3):
                for q in range(-2,3):
                    if 0<=i+r<h and 0<=j+q<w and dp[i][j] != dp[i+r][j+q] and dp[i+r][j+q]:
                        path[dp[i][j]].add(dp[i+r][j+q])
    st = dp[x1-1][y1-1]
    en = dp[a1-1][b1-1]
    curr = deque([st])
    visi = {st}
    ans=fl=0
    val = 1
    tar = 0
    val1 = 0
    while len(curr):
        x = curr.popleft()
        tar += 1
        if x == en:
            fl = 1
            break
        for i in path[x]:
            if i not in visi:
                visi.add(i)
                curr.append(i)
                val1 += 1
        if tar == val:
            tar = 0
            val = val1
            val1 = 0
            ans += 1
    if fl:
        print(ans)
    else:
        print(-1)


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