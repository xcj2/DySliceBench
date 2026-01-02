# by the authority of GOD     author: manhar singh sachdev #

import os,sys
from io import BytesIO, IOBase
from collections import deque

def update(seg_tree,value,index,x):
    curr = deque([(1,1,x)])
    while len(curr):
        y = curr.popleft()
        if y[1] <= index <= y[2]:
            seg_tree[y[0]] = max(seg_tree[y[0]],value)
            if y[1] != y[2]:
                curr.append((2*y[0],y[1],(y[1]+y[2])//2))
                curr.append((2*y[0]+1,(y[1]+y[2])//2+1,y[2]))

def traversal(seg_tree,l,r,x):
    curr = deque([(1,1,x)])
    ans = 0
    while len(curr):
        y = curr.popleft()
        if y[1]>=l and y[2]<=r:
            ans = max(ans,seg_tree[y[0]])
        elif not(y[1]>r or y[2]<l):
            curr.append((2*y[0],y[1],(y[1]+y[2])//2))
            curr.append((2*y[0]+1,(y[1]+y[2])//2+1,y[2]))
    return ans

def main():
    n,k = map(int,input().split())
    x = 524288
    seg_tree = [0]*(2*x)
    for _ in range(n):
        y = int(input())+1
        an = traversal(seg_tree,max(1,y-k),min(x,y+k),x)
        update(seg_tree,an+1,y,x)
    print(seg_tree[1])

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