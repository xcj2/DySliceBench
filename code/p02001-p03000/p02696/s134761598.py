# 具体例を試す
import math
import sys
import os
from operator import mul

sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(_S())
def LS(): return list(_S().split())
def LI(): return list(map(int,LS()))

if os.getenv("LOCAL"):
    inputFile = basename_without_ext = os.path.splitext(os.path.basename(__file__))[0]+'.txt'
    sys.stdin = open(inputFile, "r")
INF = float("inf")

A,B,N = LI()
# ans = 0

# a = [0]*N

# for x in range(1,N+1):
#     # ans = max(ans,math.floor(A*x/B) - A * math.floor(x/B))
#     a[x-1]=math.floor(A*x/B) - A * math.floor(x/B)

x = min(N,B-1)
ans = math.floor(A*x/B) - A * math.floor(x/B)
print(ans)