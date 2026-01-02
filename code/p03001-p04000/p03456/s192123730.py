import bisect,collections,copy,heapq,itertools,math,numpy,string,decimal
import sys
def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def SS(): return map(str,sys.stdin.readline().rstrip().split())
def II(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

def is_square_num(n):
  i2 = 0
  for i in range(0, n + 1):
    if i2 == n:
      return True
    if i2 > n:
      return False
    i2 += i * 2 + 1

a,b = SS()
N = int(a + b)

if is_square_num(N):
  print("Yes")
else:
  print("No")
