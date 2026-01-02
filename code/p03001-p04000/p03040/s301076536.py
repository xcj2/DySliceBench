# -*- coding: utf-8 -*-

#############
# Libraries #
#############

import sys
input = sys.stdin.readline

import math
#from math import gcd
import bisect
import heapq
from collections import defaultdict
from collections import deque
from collections import Counter
from functools import lru_cache

#############
# Constants #
#############

MOD = 10**9+7
INF = float('inf')
AZ = "abcdefghijklmnopqrstuvwxyz"

#############
# Functions #
#############

######INPUT######
def I(): return int(input().strip())
def S(): return input().strip()
def IL(): return list(map(int,input().split()))
def SL(): return list(map(str,input().split()))
def ILs(n): return list(int(input()) for _ in range(n))
def SLs(n): return list(input().strip() for _ in range(n))
def ILL(n): return [list(map(int, input().split())) for _ in range(n)]
def SLL(n): return [list(map(str, input().split())) for _ in range(n)]


#####Shorten#####
def DD(arg): return defaultdict(arg)

#####Inverse#####
def inv(n): return pow(n, MOD-2, MOD)

######Combination######
kaijo_memo = []
def kaijo(n):
  if(len(kaijo_memo) > n): return kaijo_memo[n]
  if(len(kaijo_memo) == 0): kaijo_memo.append(1)
  while(len(kaijo_memo) <= n): kaijo_memo.append(kaijo_memo[-1] * len(kaijo_memo) % MOD)
  return kaijo_memo[n]

gyaku_kaijo_memo = []
def gyaku_kaijo(n):
  if(len(gyaku_kaijo_memo) > n): return gyaku_kaijo_memo[n]
  if(len(gyaku_kaijo_memo) == 0): gyaku_kaijo_memo.append(1)
  while(len(gyaku_kaijo_memo) <= n): gyaku_kaijo_memo.append(gyaku_kaijo_memo[-1] * pow(len(gyaku_kaijo_memo),MOD-2,MOD) % MOD)
  return gyaku_kaijo_memo[n]

def nCr(n,r):
  if n == r: return 1
  if n < r or r < 0: return 0
  ret = 1
  ret = ret * kaijo(n) % MOD
  ret = ret * gyaku_kaijo(r) % MOD
  ret = ret * gyaku_kaijo(n-r) % MOD
  return ret

######Factorization######
def factorization(n):
  arr = []
  temp = n
  for i in range(2, int(-(-n**0.5//1))+1):
    if temp%i==0:
      cnt=0
      while temp%i==0: 
        cnt+=1 
        temp //= i
      arr.append([i, cnt])
  if temp!=1: arr.append([temp, 1])
  if arr==[]: arr.append([n, 1])
  return arr

#####MakeDivisors######
def make_divisors(n):
  divisors = []
  for i in range(1, int(n**0.5)+1):
    if n % i == 0:
      divisors.append(i)
      if i != n // i: 
        divisors.append(n//i)
  return divisors

#####MakePrimes######
def make_primes(N):
  max = int(math.sqrt(N))
  seachList = [i for i in range(2,N+1)]
  primeNum = []
  while seachList[0] <= max:
    primeNum.append(seachList[0])
    tmp = seachList[0]
    seachList = [i for i in seachList if i % tmp != 0]
  primeNum.extend(seachList)
  return primeNum

#####GCD#####
def gcd(a, b):
    while b: a, b = b, a % b
    return a

#####LCM#####
def lcm(a, b):
    return a * b // gcd (a, b)

#####BitCount#####
def count_bit(n):
  count = 0
  while n:
    n &= n-1
    count += 1
  return count

#####ChangeBase#####
def base_10_to_n(X, n):
  if X//n: return base_10_to_n(X//n, n)+[X%n]
  return [X%n]

def base_n_to_10(X, n):
  return sum(int(str(X)[-i-1])*n**i for i in range(len(str(X))))

def base_10_to_n_without_0(X, n):
  X -= 1
  if X//n: return base_10_to_n_without_0(X//n, n)+[X%n]
  return [X%n]

#####IntLog#####
def int_log(n, a):
  count = 0
  while n>=a:
    n //= a
    count += 1
  return count

#############
# Main Code #
#############
Q = I()
data = ILL(Q)

As = {-10**10,10**10}
for temp in data:
  if len(temp) == 3:
    As.add(temp[1])
    
As = list(As)
As.sort()

dic = DD(int)
for i in range(len(As)):
  dic[As[i]] = i 
  
class BIT:
  def __init__(self, logn):
    self.n = 1<<logn
    self.data = [0]*(self.n+1)
    self.el = [0]*(self.n+1)
  def sum(self, i):
    s = 0
    while i > 0:
      s += self.data[i]
      i -= i & -i
    return s
  def add(self, i, x):
    # assert i > 0
    self.el[i] += x
    while i <= self.n:
      self.data[i] += x
      i += i & -i
  def get(self, i, j=None):
    if j is None:
      return self.el[i]
    return self.sum(j) - self.sum(i)
  def bisect(self, x):
    w = i = 0
    k = self.n
    while k:
      if i+k <= self.n and w + self.data[i+k] < x:
        w += self.data[i+k]
        i += k
      k >>= 1
    return i+1

class BIT_RSQ_RAQ:
  def __init__(self, N):
    self.N = N
    self.data0 = [0]*(self.N+1)
    self.data1 = [0]*(self.N+1)
  def _add(self, data, k, x):
    while k <= self.N:
      data[k] += x
      k += k & -k
  def add(self, l, r, x):
    self._add(self.data0, l, -x*(l-1))
    self._add(self.data0, r, x*(r-1))
    self._add(self.data1, l, x)
    self._add(self.data1, r, -x)
  def _get(self, data, k):
    s = 0
    while k:
      s += data[k]
      k -= k & -k
    return s
  def query(self, l, r):
    return self._get(self.data1, r-1) * (r-1) + self._get(self.data0, r-1) - self._get(self.data1, l-1) * (l-1) - self._get(self.data0, l-1)

N = len(As)
B = BIT(int_log(N,2)+1)
ACC1 = BIT_RSQ_RAQ(N)
ACC2 = BIT_RSQ_RAQ(N)

base = 0
count = 0
for temp in data:
  if len(temp) == 3:
    _,a,b = temp
    ACC1.add(1,dic[a]+1,a+10**10)
    ACC2.add(dic[a]+2,N+1,10**10-a)
    base += b
    count += 1
    B.add(dic[a],1)
  else:
    x = As[B.bisect((count+1)//2)]
    #print(x,ACC1.query(dic[x]+1,dic[x]+2),(x+10**10),(count-B.sum(dic[x])),ACC2.query(dic[x]+1,dic[x]+2),(10**10-x),(B.sum(dic[x]-1)),base)
    print(x,ACC1.query(dic[x]+1,dic[x]+2)-(x+10**10)*(count-B.sum(dic[x]))+ACC2.query(dic[x]+1,dic[x]+2)-(10**10-x)*(B.sum(dic[x]-1))+base)
    
    
    