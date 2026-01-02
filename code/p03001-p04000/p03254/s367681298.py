import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def SS(): return map(str,sys.stdin.readline().rstrip().split())
def II(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

N,x = II()
a = LI()
a.sort()
cnt = 0
for ai in a:
  if x > ai:
    x -= ai
    cnt += 1
  elif x == ai:
    cnt += 1
    x -= ai
    break
  else:
    cnt += 1
    break
if x != 0:
  cnt -= 1
print(cnt)