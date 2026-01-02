import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def SS(): return map(str,sys.stdin.readline().rstrip().split())
def II(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

def f(n):
  if n % 2 == 0:
    return n/2
  else:
    return 3*n + 1

s = I()
a = {s}


for i in range(2,1000001):
  ai = f(s)
  if ai in a:
    print(i)
    exit()
  s = ai
  a.add(ai)
