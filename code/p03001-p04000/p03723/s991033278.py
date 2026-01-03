import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def SS(): return map(str,sys.stdin.readline().rstrip().split())
def II(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

A,B,C = II()


if A==B==C and A % 2 != 1:
  print(-1)
  exit()
cnt = 0
while A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
  A_half = A/2
  B_half = B/2
  C_half = C/2
  A = B_half + C_half
  B = A_half + C_half
  C = A_half + B_half
  cnt += 1
print(cnt)
