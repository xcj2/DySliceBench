import sys
from itertools import combinations
sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808
MOD = 1000000007
def POW(x, y): return pow(x, y, MOD)
def INV(x, m=MOD): return pow(x, m - 2, m)
def DIV(x, y, m=MOD): return (x * INV(y, m)) % m
def LI(): return [int(x) for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()
def II(): return int(input())

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


N=II()
INL=[tuple(LI()) for i in range(N)]
INL.sort()

if N == 1:
    print(1)
    exit()
elif N == 2:
    print(1)
    exit()
elif N > 2:
    res = INTMAX
    for ptr1, ptr2 in combinations(INL,2):
        union = UnionFindTree(N)
        dx, dy = ptr2[0]-ptr1[0], ptr2[1]-ptr1[1] 
        for i in range(N):
            for j in range(i, N):
                if INL[i][0] + dx == INL[j][0] and INL[i][1]+dy == INL[j][1]:
                    union.unite(i,j)
        st = set()
        for i in range(N):
            st.add(union.find(i))
        res = min(res,len(st))
    print(res)
