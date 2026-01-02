import sys
import itertools
import bisect
from operator import itemgetter
 
MAX_INT = int(10e15)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()
def combi(n, r):
  r = min(r, n-r)
  numer = denom = 1
  for i in range(1, r+1):
    numer = numer * (n+1-i) %mod
    denom = denom * i %mod
  return numer * pow(denom, mod-2, mod) %mod
N = I()
a = IL()

dic = {}
for i in a:
  if i in dic:
    dic[i] += 1
  else:
    dic[i] = 1

ans = 0
for i in dic.values():
  ans += i*(i-1)//2

for i in a:
  n = dic[i]
  print(ans - n*(n-1)//2 + (n-1)*(n-2)//2 )