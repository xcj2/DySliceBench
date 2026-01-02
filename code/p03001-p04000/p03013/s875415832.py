import sys,collections,math,random;sys.setrecursionlimit(10**7)
def Is(): return [int(x) for x in sys.stdin.readline().split()]
def Ss(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

MOD = 10**9 + 7
n,m = Is()
ns = [0] * (n+1)
ns[0] = 1
for i in range(m):
    ns[I()] = -1
for i in range(n):
    if ns[i] >= 0 and i+1 <= n and ns[i+1] >= 0:
        ns[i+1] = (ns[i+1] + ns[i]) % MOD
    if ns[i] >= 0 and i+2 <= n and ns[i+2] >= 0:
        ns[i+2] = (ns[i+2] + ns[i]) % MOD
print(ns[n])
    	