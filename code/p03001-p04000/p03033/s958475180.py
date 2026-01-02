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
    mod = 10**9 + 7

    n, q = map(int, input().split())
    stx = []
    for _ in range(n):
        s, t, x = map(int, input().split())
        stx.append([x, s - x, t - x])
    stx.sort(reverse=True)
    d = [int(input()) for _ in range(q)]

    N = q
    N0 = 2**(N-1).bit_length()
    data = [None]*(2*N0)
    INF = (-1, 10**9 + 1)
    def update(l, r, v):
        L = l + N0; R = r + N0
        while L < R:
            if R & 1:
                R -= 1
                data[R-1] = v

            if L & 1:
                data[L-1] = v
                L += 1
            L >>= 1; R >>= 1
    def _query(k):
        k += N0-1
        s = INF
        while k >= 0:
            if data[k]:
                s = max(s, data[k])
            k = (k - 1) // 2
        return s
    def query(k):
        return _query(k)[1]



    import bisect

    for i, (x, start, last) in enumerate(stx):
        l = bisect.bisect_left(d, start)
        r = bisect.bisect_left(d, last)
        update(l, r, (i, x))

    for i in range(q):
        res = query(i)
        if res == 10**9 + 1:
            print(-1)
        else:
            print(res)

main()
