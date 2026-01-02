import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def SS(): return map(str,sys.stdin.readline().rstrip().split())
def II(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()
A = LI()
cnt = 0
if len(A) != len([a for a in A if a % 2 == 0]):
  print(0)
  exit()

while True:
  cnt += 1
  A = [a / 2 for a in A]
  if len(A) != len([a for a in A if a % 2 == 0]):
    break
print(cnt)