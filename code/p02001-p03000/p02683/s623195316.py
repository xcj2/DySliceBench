#------------------------------warmup----------------------------
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
 
#-------------------game starts now-----------------------------------------------------
n,m,x=map(int,input().split())
e=[]
tot=999999999999999999999999999
def binary(n,ju):
    binaryNum = [0] * (ju) 
    i = 0
    while (n > 0):  
        binaryNum[i] = n % 2 
        n = int(n / 2) 
        i += 1 
    binaryNum.reverse()
    return binaryNum
for i in range(n):
    e.append(list(map(int,input().split())))
for i in range(0,2**(n)):
    ans=[0]*m
    s=binary(i,n)
    cost=0
    #print(s)
    for j in range(n):
        if s[j]==1:
            cost+=e[j][0]
            for k in range(m):
                ans[k]+=e[j][k+1]
    f=0
    for j in ans:
        if j<x:
            f=1
            break
    if f==0:
        tot=min(tot,cost)
if tot==999999999999999999999999999: 
    print(-1)
else:
    print(tot)