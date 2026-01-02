def main():
    import os
    import sys
    from io import BytesIO, IOBase
    
    BUFSIZE = 8192
    
    
    class FastIO(IOBase):
        newlines = 0
    
        def __init__(self, file):
            self._fd = file.fileno()
            self.buffer = BytesIO()
            self.writable = "x" in file.mode or "r" not in file.mode
            self.write = self.buffer.write if self.writable else None
    
        def read(self):
            while 1:
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
    mod = 10**9 + 7


            

    h, w = map(int, input().split())
    a = [[int(x) for x in input().split()] for _ in range(h)]
    b = [[int(x) for x in input().split()] for _ in range(h)]
    c = [[0]*w for _ in range(h)]
    max_value = 80 * (h + w)
    for i in range(h):
        for j in range(w):
            c[i][j] = abs(a[i][j] - b[i][j])
    dp = [[[0]*(max_value + 1) for _ in range(w)] for _ in range(h)]
    dp[0][0][c[0][0]] = 1
    for i in range(h):
        for j in range(w):
            for k in range(max_value + 1):
                # print(i, j, k, k + c[i][j + 1])
                if 0 <= i + 1 < h and dp[i][j][k]:
                    if 0 <= k + c[i + 1][j] <= max_value:
                        dp[i + 1][j][k + c[i + 1][j]] = 1
                    if 0 <= abs(k - c[i + 1][j]) <= max_value:
                        dp[i + 1][j][abs(k - c[i + 1][j])] = 1
                if 0 <= j + 1 < w and dp[i][j][k]:
                    if 0 <= k + c[i][j + 1] <= max_value:
                        dp[i][j + 1][k + c[i][j + 1]] = 1
                    if 0 <= abs(k - c[i][j + 1]) <= max_value:
                        dp[i][j + 1][abs(k - c[i][j + 1])] = 1
    for k in range(max_value + 1):
        if dp[h - 1][w - 1][k]:
            print(k)
            sys.exit()
main()



