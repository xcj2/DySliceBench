import os
import heapq
import sys,threading
import math as mt
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
dic={}
def lcm(num1,num2):
    return (num1*num2)//gcd(num1,num2)

# Python3 program to find prime factorization
# of a number n in O(Log n) time with
# precomputation allowed.


MAXN = 10**6+1

# stores smallest prime factor for
# every number
spf = [0 for i in range(MAXN)]


# Calculating SPF (Smallest Prime Factor)
# for every number till MAXN.
# Time Complexity : O(nloglogn)
def sieve():
    spf[1] = 1
    for i in range(2, MAXN):
        spf[i] = i

    # separately marking spf for
    # every even number as 2
    for i in range(4, MAXN, 2):
        spf[i] = 2

    for i in range(3, mt.ceil(mt.sqrt(MAXN))):

        # checking if i is prime
        if (spf[i] == i):

            # marking SPF for all numbers
            # divisible by i
            for j in range(i * i, MAXN, i):
                if (spf[j] == j):
                    spf[j] = i

                # A O(log n) function returning prime


# factorization by dividing by smallest
# prime factor at every step
def getFactorization(x):
    ret = defaultdict(int)
    while x != 1:
        ret[spf[x]]+=1
        x = x // spf[x]

    return ret

#
# # Driver code
#
# # precalculating Smallest Prime Factor
#
# x = 12246
# print("prime factorization for", x, ": ",
#       end="")
#
# # calling getFactorization function
# p = getFactorization(x)
#
# for i in range(len(p)):
#     print(p[i], end=" ")


# This code is contributed
# by Mohit kumar 29


def main():
    #t=int(input())
    global dic
    t=1
    for _ in range(t):
        n=int(input())
        arr=inar()
        sieve()
        coprime=True
        dic=defaultdict(int)
        for i in range(n):
            take=getFactorization(arr[i])
            #print(take)
            for key in take.keys():
                dic[key]+=1
                if dic[key]>1:
                    coprime=False
                    break
            if coprime==False:
                break
        if coprime:
            print("pairwise coprime")
        else:
            gc=arr[0]
            for i in range(n):
                gc=gcd(arr[i],gc)
            if gc==1:
                print("setwise coprime")
            else:
                print("not coprime")





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
