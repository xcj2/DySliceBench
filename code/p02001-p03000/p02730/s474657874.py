import sys
import os
import time
import collections
from collections import Counter, deque
import itertools
import math
import timeit
import random
from io import BytesIO, IOBase
 
#########################
# imgur.com/Pkt7iIf.png #
#########################
 
def sieve(n):
    if n < 2: return list()
    prime = [True for _ in range(n + 1)]
    p = 3
    while p * p <= n:
        if prime[p]:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 2
    r = [2]
    for p in range(3, n + 1, 2):
        if prime[p]:
            r.append(p)
    return r
 
def divs(n, start=1):
    divisors = []
    for i in range(start, int(math.sqrt(n) + 1)):
        if n % i == 0:
            if n / i == i:
                divisors.append(i)
            else:
                divisors.extend([i, n // i])
    return divisors
 
def divn(n, primes):
    divs_number = 1
    for i in primes:
        if n == 1:
            return divs_number
        t = 1
        while n % i == 0:
            t += 1
            n //= i
        divs_number *= t
 
def flin(d, x, default=-1):
    left = right = -1
    for i in range(len(d)):
        if d[i] == x:
            if left == -1: left = i
            right = i
    if left == -1:
        return (default, default)
    else:
        return (left, right)
 
def ceil(n, k): return n // k + (n % k != 0)
def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(map(int, input().split()))
def lcm(a, b): return abs(a * b) // math.gcd(a, b)
def prr(a, sep=' '): print(sep.join(map(str, a)))
def dd(): return collections.defaultdict(int)
def ddl(): return collections.defaultdict(list)
 
 
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
'''for _ in range(ii()):
    n=ii()
    a=li()
    m,k,md=0,0,0
    mn,mx=10**9+1,-10**9-1
    for i in range(n-1):
        if a[i]!=-1 and a[i+1]!=-1:
            m=max(m,abs(a[i]-a[i+1]))
    for i in range(1,n-1):
        if a[i]==-1:
            if a[i+1]!=-1:
                mn=min(mn,a[i+1])
                mx=max(mx,a[i+1])
            if a[i-1]!=-1:
                mn=min(mn,a[i-1])
                mx=max(mx,a[i-1])
    if mn==10**9+1 and mx==-10**9-1:
        print(0,0,sep=' ')
    else:
        md=(mn+mx+1)//2
        m=max(abs(mx-md),abs(mn-md),m)
        print(m,md,sep=' ')'''

'''for _ in range(ii()):
    n,m=mi()
    tg=n//2
    n0=n-m
    total=(n*(n+1))//2
    res=0
    if n0<n:
        if m>=tg:
            res=total-n0
        else:
            i=tg-m
            if n&1:
                nn0=2*i+1
            else:
                nn0=2*i
            res=total-((nn0*(nn0+1))//2)-(n0-nn0)
            #print(nn0,n0-nn0)
    print(res)'''
#***************************************************************************************************************************


'''def solve():
    n=int(input())
    a=list(map(int,input().split()))
    diff=len(set(a))
    if diff==1: print (int((n*(n+1))/2))
    elif diff==n: print (1)
    else:
        i=j=ans=0
        ahead=True
        distinct={}
        while j<n:
            if ahead:
                distinct[a[j]]=distinct[a[j]]+1 if a[j] in distinct else 1
                if len(distinct)==diff:
                    ahead=False
                else:
                    j+=1
            else:
                ans+=n-j
                if distinct[a[i]]>1:
                    distinct[a[i]]-=1
                else:
                    distinct.pop(a[i])
                    j+=1
                    ahead=True
                i+=1
        print (ans)
 
solve()'''

#******************************************************************************************

'''s=input()
n=len(s)
i,cntl,cntg=0,0,0
res,fl,fg=0,0,0
while(i<n):
    if s[i]=='<':
        while(i<n and s[i]!='>'):
            fl=1
            cntl+=1
            i+=1
    else:
        while(i<n and s[i]!='<'):
            fg=1
            cntg+=1
            i+=1
    if fl==1 and fg==1:
        res+=max(cntl,cntg)
        cntl-=1
        cntg-=1
        res+=cntl*(cntl+1)//2
        res+=cntg*(cntg+1)//2
        fl,fg,cntl,cntg=0,0,0,0
if fl:
    res+=cntl*(cntl+1)//2
if fg:
    res+=cntg*(cntg+1)//2
print(res)'''


#********************************************************************************************************

def isPalindrome(s):
    return s==s[::-1]
s=input()
n=len(s)
f=0
if isPalindrome(s) and isPalindrome(s[:n//2]) and isPalindrome(s[(n+2)//2:]):
    f=1
else:
    f=0
if f==1:
    print('Yes')
else:
    print('No')