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


    n, m, s = map(int, input().split())
    s = min(s, 2500)
    from collections import defaultdict
    # O(ElogV)
    import heapq
    def dijkstra(s, x):
        # 始点sから各頂点への最短距離
        d = defaultdict(lambda: float("inf"))
        d[(s, x)] = 0
        # 各頂点が訪問済みかどうか
        used = defaultdict(lambda: False)
        used[(s, x)] = True
        # 仮の距離を記録するヒープ
        que = []
        for e in edge[(s, x)]:
            heapq.heappush(que, e)
        while que:
            minedge = heapq.heappop(que)
            if used[minedge[1]]:
                continue
            v = minedge[1]
            d[v] = minedge[0]
            used[v] = True
            for e in edge[v]:
                if not used[e[1]]:
                    heapq.heappush(que, (e[0] + d[v], e[1]))
        return d

    max_money = 2500
    edge = defaultdict(list)
    for _ in range(m):
        u, v, a, b = map(int, input().split())
        u -= 1
        v -= 1
        for i in range(a, max_money + 1):
            edge[(u, i)].append((b, (v, i - a)))
            edge[(v, i)].append((b, (u, i - a)))
    for j in range(n):
        c, d = map(int, input().split())
        for i in range(max_money):
            if i + c <= max_money:
                edge[(j, i)].append((d, (j, i + c)))

    ans = [10**18]*n

    d = dijkstra(0, s)
    for i in d:
        x, y = i
        cost = d[i]
        ans[x] = min(ans[x], cost)
    for i in ans[1:]:
        print(i)
main()
