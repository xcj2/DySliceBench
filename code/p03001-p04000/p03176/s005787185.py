# by the authority of GOD     author: manhar singh sachdev #

import os,sys
from io import BytesIO, IOBase
from collections import deque

def update(seg_tree,val,update_val,x):
    curr = deque([(1,x,1)])
    while len(curr):
        y = curr.popleft()
        if y[0]<=val<=y[1]:
            seg_tree[y[2]] = max(seg_tree[y[2]],update_val)
            if y[0]!=y[1]:
                curr.append((y[0],(y[0]+y[1])//2,2*y[2]))
                curr.append(((y[0]+y[1])//2+1,y[1],2*y[2]+1))

def trav(seg_tree,val,x):
    curr = deque([(1,x,1)])
    ans = 0
    while len(curr):
        y = curr.popleft()
        if y[1]<val:
            ans = max(ans,seg_tree[y[2]])
        elif y[0]<=val<=y[1] and y[0]!=y[1]:
            curr.append((y[0],(y[0]+y[1])//2,2*y[2]))
            curr.append(((y[0]+y[1])//2+1,y[1],2*y[2]+1))
    return ans

def main():
    n = int(input())
    h = list(map(int,input().split()))
    a = list(map(int,input().split()))
    x = 1<<n.bit_length()
    seg_tree = [0]*(x<<1)
    fin = 0
    for i in range(n):
        k = trav(seg_tree,h[i],x)
        fin = max(fin,a[i]+k)
        update(seg_tree,h[i],a[i]+k,x)
    print(fin)

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