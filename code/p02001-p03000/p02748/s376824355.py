import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def SS(): return map(str,sys.stdin.readline().rstrip().split())
def II(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

A,B,M = II()
a = LI()
b = LI()
ticket = [LI() for _ in range(M)]

cost = min(a) + min(b)
costl = [a[t[0]-1] + b[t[1]-1] - t[2] for t in ticket]

print(min(cost,min(costl)))