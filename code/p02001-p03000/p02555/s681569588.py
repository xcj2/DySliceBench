import os
import heapq
import sys,threading
import math
import bisect
import operator
from collections import defaultdict
sys.setrecursionlimit(10**5)
from io import BytesIO, IOBase
def gcd(a,b):
    if b==0:

        return a
    else:
        return gcd(b,a%b)
def power(x, p,m):
    res = 1
    while p:
        if p & 1:
            res = (res * x) % m
        x = (x * x) % m
        p >>= 1
    return res
def inar():
    return [int(k) for k in input().split()]

def lcm(num1,num2):
    return (num1*num2)//gcd(num1,num2)
# Python3 function to
# calculate nCr % p
def ncr(n, r, p):
	# initialize numerator
	# and denominator
	num = den = 1
	for i in range(r):
		num = (num * (n - i)) % p
		den = (den * (i + 1)) % p
	return (num * pow(den,
			p - 2, p)) % p

# p must be a prime
# greater than n
# n, r, p = 10, 2, 13
# print("Value of nCr % p is",
# 			ncr(n, r, p))


def main():
    # n=int(input())
    mod=10**9+7
    #
    # # print(fact)
    # if n==1:
    #     print(0)
    # else:
    #     take=(ncr(n,2,mod)*ncr(n,n-2,mod)*power(10,n-2,mod))%mod
    #     print(take)
    #     # ans=0
    #     # for i in range(2,n):
    #     #     ans=(ans+power(10,n-i-1,mod))%mod
    #     # print(ans)
    n=int(input())
    dp=[0,0,0,1]
    for i in range(4,n+1):
        ans=0
        for j in range(3,i+1):
            ans+=dp[i-j]
        dp.append(1+ans)
    print(dp[n]%mod)


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
    #threadin.Thread(target=main).start()
