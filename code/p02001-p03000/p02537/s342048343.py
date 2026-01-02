import os, sys
from io import IOBase, BytesIO
py2 = round(0.5)
if py2:
    from future_builtins import ascii, filter, hex, map, oct, zip
    range = xrange
BUFSIZE = 8192
class FastIO(BytesIO):
    newlines = 0
 
    def __init__(self, file):
        self._file = file
        self._fd = file.fileno()
        self.writable = 'x' in file.mode or 'w' in file.mode
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
            s = self._fill(); self.newlines = s.count(b'\n') + (not s)
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
 
# Cout implemented in Python
import sys
class ostream:
    def __lshift__(self,a):
        sys.stdout.write(str(a))
        return self
cout = ostream()
endl = '\n'

class SegTree():
    def __init__(self, n_val, init_ele, combiner):
        self.n_val = n_val
        self.n = 1 << (self.n_val - 1).bit_length()
        self.tree = [init_ele] * (2 * self.n)
        self.combiner = combiner
        self.init_ele = init_ele

    def init_tree(self, data):
        self.data = data
        for x in range(self.n):
            self.tree[x + n] = self.data[x]
        for x in range(self.n - 1, 0, -1):
            self.tree[x] = self.combiner(self.tree[x<<1], self.tree[(x<<1) + 1])

    def query(self, l, r):
        l = l + self.n
        r = r + self.n
        res = self.init_ele
        while l < r:
            if l & 1:
                res = self.combiner(res, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res = self.combiner(res, self.tree[r])
            l = l >> 1
            r = r >> 1
        return res

    def update_single(self, idx, val):
        idx += self.n
        self.tree[idx] = val
        while idx > 0:
            self.tree[idx>>1] = self.combiner(self.tree[idx], self.tree[idx ^ 1])
            idx >>= 1


def solve():
    
    n, k = map(int, input().split())

    n_val = 3 * (10 ** 5)

    arr = [int(input()) for _ in range(n)]
    s_tree = SegTree(n_val, 0, max)

    for a in arr:
        s_tree.update_single(a, s_tree.query(max(a - k, 0), min(a + k, n_val) + 1) + 1)
    cout<<s_tree.query(1, n_val + 1)<<endl






def main():
    solve()


if __name__ == "__main__":
    main()