import math
import sys
import os

sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(_S())
def LS(): return list(_S().split())
def LI(): return list(map(int,LS()))

if os.getenv("LOCAL"):
    inputFile = basename_without_ext = os.path.splitext(os.path.basename(__file__))[0]+'.txt'
    sys.stdin = open(inputFile, "r")
INF = float("inf")

def divisor_count(n):
    divisors = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors += 1
            if i != n // i:
                divisors += 1  
    return divisors    

N = I()
ans = 0

# for i in range(1,N):
#     ans += divisor_count(i)

for i in range(1,N):
    ans += (N-1)//i

print(ans)