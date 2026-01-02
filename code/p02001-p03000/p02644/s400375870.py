import os
import heapq
import sys
import math
import operator
from collections import defaultdict, deque
from io import BytesIO, IOBase


"""def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)"""

"""def pw(a,b):
    result=1
    while(b>0):
        if(b%2==1): result*=a
        a*=a
        b//=2
    return result"""



def inpt():
    return [int(k) for k in input().split()]


def main():
    n,m,k=map(int,input().split())
    x1,y1,x2,y2=map(int,input().split())
    ar=[]
    ans=[]
    visited=[]
    for i in range(n):
        visited.append([False]*m)
        ar.append(input())
        ans.append([0]*m)

    if(ar[x1-1][y1-1]=='@' or ar[x2-1][y2-1]=='@'):
        print(-1)
    q=deque()
    q.append((x1-1,y1-1))
    br=[(-1,0),(1,0),(0,1),(0,-1)]
    #ar[x1-1][y1-1]=1000000000
    while(q):
        a,b=q.popleft()
        #print(a,b)
        if(a==x2-1 and b==y2-1):
            print(ans[a][b])
            exit()
        for p,r in br:
            for i in range(1,k+1):
                x=a+i*p
                y=b+i*r
                if not (0<=x<n and 0<=y<m) or ar[x][y]=='@' or (x==x1-1 and y==y1-1):
                    break
                if(0<ans[x][y]<=ans[a][b]):
                    break
                #print('>>>', x, y, ans[x][y])
                ans[x][y]=ans[a][b]+1
                #print('>>>', x, y, ans[x][y])
                if(not visited[x][y]):
                    q.append([x,y])
                    visited[x][y]=True
    print(-1)







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

if __name__ == "__main__":
    main()
