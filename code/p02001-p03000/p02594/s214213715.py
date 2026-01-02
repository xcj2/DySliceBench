# for #!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase


# region fastio

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

# endregion
class union_find:
    def __init__(self, n):
        self.n = n
        self.rank = [0]*n
        self.parent = [int(j) for j in range(n)]
    
    def union(self,i,j):
        i = self.find(i)
        j = self.find(j)
        if self.rank[i] == self.rank[j]:
            self.parent[i] = j
            self.rank[j] += 1

        elif self.rank[i] > self.rank[j]:
            self.parent[j] = i
        else:
            self.parent[i] = j

    def find(self, i):
        temp = i
        if self.parent[temp] != temp:
            self.parent[temp] = self.find(self.parent[temp])
        return self.parent[temp]
from math import log2, ceil
def main():
# Enter your code here. Read input from STDIN. Print output to STDOUT
    # for t in range(int(input())):
        n = int(input())
        # n,k  =[int(j) for j in input().split()]
        if(n>=30):
            print("Yes")
        else:
            print("No")

        # print(m)
        


        # n,k,z  =[int(j) for j in input().split()]
        



if __name__ == "__main__":
    main()