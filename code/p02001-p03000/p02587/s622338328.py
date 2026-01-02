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

N = I()
data = SLL(N)
words = []
costs = []
nodes = {("",0),("",1)}

best = INF
for d in data:
  word = d[0]
  cost = int(d[1])
  if word == word[::-1]:
    best = min(best,cost)
    continue
  words.append(word)
  costs.append(cost)
  for j in range(len(word)):
    nodes.add((word[:j+1],1))
    nodes.add((word[j:],0))
    
graph = {k:[] for k in nodes}
graph[("",1)].append((0,("",0)))
for k in nodes:
  amari = k[0]
  t = k[1]
  if amari == amari[::-1]:
    if amari:
      graph[k].append((0,("",0)))
  else:
    n = len(amari)
    for i in range(len(words)):
      word = words[i]
      cost = costs[i]
      if t == 0:
        if len(word)>n:
          if amari == word[::-1][:n]:
            graph[k].append((cost,(word[:-n],1)))
        else:
          if amari[:len(word)] == word[::-1]:
            graph[k].append((cost,(amari[len(word):],0)))
      else:
        if len(word)>n:
          if amari[::-1] == word[:n]:
            graph[k].append((cost,(word[n:],0)))
        else:
          if amari[::-1][:len(word)] == word:
            graph[k].append((cost,(amari[:-len(word)],1)))

def dijkstra(graph, start,cost):
  N = len(graph)
  d = {k:INF for k in nodes}
  d[start] = cost
  f = {k:False for k in nodes}
  q = [(cost, start)]
  while q:
    c,u = heapq.heappop(q)
    if f[u]: continue
    d[u] = c
    f[u] = True
    for c,v in graph[u]:
      if not f[v]:
        heapq.heappush(q, (c + d[u], v))
  return d   

for i in range(len(words)):
  word = words[i]
  cost = costs[i]
  best = min(best,dijkstra(graph,(word,0),cost)[("",0)])
  best = min(best,dijkstra(graph,(word,1),cost)[("",0)])
  
if best == INF:
  print(-1)
else:
  print(best)