# -*- coding: utf-8 -*-

#############
# Libraries #
#############

import sys
input = sys.stdin.readline

import math
#from math import gcd
import bisect
from collections import defaultdict
from collections import deque
from functools import lru_cache


#############
# Constants #
#############

MOD = 10**9+7
INF = float('inf')

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

######OUTPUT######
def P(arg): print(arg); return
def Y(): print("Yes"); return
def N(): print("No"); return
def E(): exit()
def PE(arg): print(arg); exit()
def YE(): print("Yes"); exit()
def NE(): print("No"); exit()

#####Shorten#####
def DD(arg): return defaultdict(arg)


#####Inverse#####
def inv(n): return pow(n, MOD-2, MOD)

######Combination######
kaijo_memo = []
def kaijo(n):
  if(len(kaijo_memo) > n):
    return kaijo_memo[n]
  if(len(kaijo_memo) == 0):
    kaijo_memo.append(1)
  while(len(kaijo_memo) <= n):
    kaijo_memo.append(kaijo_memo[-1] * len(kaijo_memo) % MOD)
  return kaijo_memo[n]

gyaku_kaijo_memo = []
def gyaku_kaijo(n):
  if(len(gyaku_kaijo_memo) > n):
    return gyaku_kaijo_memo[n]
  if(len(gyaku_kaijo_memo) == 0):
    gyaku_kaijo_memo.append(1)
  while(len(gyaku_kaijo_memo) <= n):
    gyaku_kaijo_memo.append(gyaku_kaijo_memo[-1] * pow(len(gyaku_kaijo_memo),MOD-2,MOD) % MOD)
  return gyaku_kaijo_memo[n]

def nCr(n,r):
  if(n == r):
    return 1
  if(n < r or r < 0):
    return 0
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
  if temp!=1:
    arr.append([temp, 1])
  if arr==[]:
    arr.append([n, 1])
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
    while b:
        a, b = b, a % b
    return a

#####LCM#####
def lcm(a, b):
    return a * b // gcd (a, b)

#####BitCount#####
def count_bit(n):
  count = 0
  while n:
    n &= n -1
    count += 1
  return count

#####ChangeBase#####
def base_10_to_n(X, n):
  if X//n:
    return base_10_to_n(X//n, n)+[X%n]
  return [X%n]

def base_n_to_10(X, n):
  return sum(int(str(X)[-i-1])*n**i for i in range(len(str(X))))

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
N = I()
R = ILL(N)
B = ILL(N)

class Dinic:
  def __init__(self, N):
    self.N = N
    self.G = [[] for _ in range(N)]
    self.level = [0 for _ in range(N)]
    self.iter = [0 for _ in range(N)]

  def add(self, from_, to, cap):
    self.G[from_].append({'to':to, 'cap':cap, 'rev':len(self.G[to])})
    self.G[to].append({'to':from_, 'cap':0, 'rev':len(self.G[from_])-1})


  def bfs(self, s):
    self.level = [-1 for _ in range(self.N)]
    self.level[s] = 0;
    q = deque([s])
    while q:
      v = q.popleft()
      for i in range(len(self.G[v])):
        e = self.G[v][i]
        if e['cap'] > 0 and self.level[e['to']] < 0:
          self.level[e['to']] = self.level[v] + 1
          q.append(e['to'])

  def dfs(self, v, t, f):
    if v == t:
      return f
    for i in range(self.iter[v], len(self.G[v])):
      self.iter[v] = i
      e = self.G[v][i]
      if e['cap'] > 0 and self.level[v] < self.level[e['to']]:
        d = self.dfs(e['to'], t, min(INF, e['cap']))
        if d > 0:
          e['cap'] -= d
          self.G[e['to']][e['rev']]['cap'] += d
          return d
    return 0

  def max_flow(self, s, t):
    flow = 0
    while True:
      self.bfs(s)
      if self.level[t] < 0:
        return flow
      self.iter = [0 for _ in range(self.N)]
      f = self.dfs(s,t,INF)
      while f > 0:
        flow += f
        f = self.dfs(s,t,INF)  
        
graph = Dinic(N*2+2)
for i in range(N):
  for j in range(N):
    if R[i][0] < B[j][0] and R[i][1] < B[j][1]:
      graph.add(i,j+N,1)
for i in range(N):
  graph.add(2*N,i,1)
  graph.add(i+N,2*N+1,1)

print(graph.max_flow(2*N,2*N+1))