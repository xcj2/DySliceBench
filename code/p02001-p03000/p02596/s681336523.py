import os
import sys
from io import BytesIO, IOBase
# from collections import defaultdict as dd
# from collections import deque as dq
# import itertools as it
# from math import sqrt, log, log2
# from fractions import Fraction
# def primeFactors(n): 
#     ans = []
#     # Print the number of two's that divide n 
#     while n % 2 == 0: 
#         ans.append(2) 
#         n = n / 2
          
#     # n must be odd at this point 
#     # so a skip of 2 ( i = i + 2) can be used 
#     for i in range(3,int(sqrt(n))+1,2): 
          
#         # while i divides n , print i ad divide n 
#         while n % i== 0: 
#             ans.append(i)
#             n = n / i 
              
#     # Condition if n is a prime 
#     # number greater than 2 
#     if n > 2: 
#         ans.append(int(n))

#     return ans 

def main():
    k = int(input())
    if k%2 == 0:
        print(-1)
    else:
        pass
    
        rem = 7%k

        ans = -1
        for i in range(1, 10**7):
            if rem == 0:
                ans = i
                break

            rem = 10*rem + 7
            rem %= k

        print(ans)

        


        




































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
 
if __name__ == "__main__":
    main()