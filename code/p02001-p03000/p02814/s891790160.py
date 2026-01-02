import sys
from math import gcd
sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし


N,M = MI()
A = LI()

x = sum(a % 2 == 0 for a in A)
if x != N:
    print(0)
    exit()

r = 0
while A[0] % 2 == 0:
    r += 1
    A[0] //= 2
for i in range(1,N):
    if A[i] % (2**r) != 0 or (A[i]//(2**r)) % 2 == 0:
        print(0)
        exit()
    else:
        A[i] //= 2**r

lcm = A[0]
for i in range(1,N):
    lcm = (lcm*A[i])//gcd(lcm,A[i])

a = (lcm*2**r)//2
print(((M//a)+1)//2)
