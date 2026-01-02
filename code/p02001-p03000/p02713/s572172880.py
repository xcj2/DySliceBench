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


K = I()
ans = 0

for i in range(1,K+1):
    for j in range(1,K+1):
        for k in range(1,K+1):
            ans += math.gcd(math.gcd(i,j),k)

print(ans)