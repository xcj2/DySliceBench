import sys
import math
import heapq
sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808
DVSR = 1000000007
def POW(x, y): return pow(x, y, DVSR)
def INV(x, m=DVSR): return pow(x, m - 2, m)
def DIV(x, y, m=DVSR): return (x * INV(y, m)) % m
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def FLIST(n):
    res = [1]
    for i in range(1, n+1): res.append(res[i-1]*i%DVSR)
    return res

class UnionFindTree:
    def __init__(self, n):
        self.nodes = list(range(n+1))
    def find(self, x):
        if self.nodes[x] == x:
            return x
        parent = self.find(self.nodes[x])
        self.nodes[x] = parent
        return parent
    def unite(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return
        self.nodes[a] = self.nodes[b]
    def is_same(self, a, b):
        return self.find(a) == self.find(b)

N,M,K=LI()
UF=UnionFindTree(N)
NUMF = [0]*(N+1)
for i in range(M):
    f,t = LI()
    UF.unite(f,t)
    NUMF[f] += 1
    NUMF[t] += 1

BLL=[]
for j in range(K):
    f, t = LI()
    BLL.append((f,t))
    BLL.append((t,f))
BLL.sort()
GPS = [0]*(N+1)

for i in range(1, N+1):
    UF.find(i)
    GPS[UF.nodes[i]] += 1

ptr = 0
K2 = 2*K
for i in range(1, N+1):
    res = GPS[UF.find(i)] - 1 - NUMF[i]
    while BLL and ptr < K2 and i == BLL[ptr][0]:
        res -= UF.is_same(BLL[ptr][0], BLL[ptr][1])
        ptr += 1
    print(res, end=" ")
print("")