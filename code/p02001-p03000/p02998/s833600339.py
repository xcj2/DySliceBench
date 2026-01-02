import sys
sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808
DVSR = 1000000007
def POW(x, y): return pow(x, y, DVSR)
def INV(x, d=DVSR): return pow(x, d - 2, d)
def DIV(x, y, d=DVSR): return (x * INV(y, d)) % d
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

UFL=UnionFindTree(100010)
UFR=UnionFindTree(100010)

N=II()
rmap = {}
lmap = {}
for i in range(N):
    l,r=LI()
    if not r in rmap:
        rmap[r] = []
    if not l in lmap:
        lmap[l] = []
    rmap[r].append(l)
    lmap[l].append(r)

for l, lis in lmap.items():
    for r in lmap[l]:
        for l2 in rmap[r]:
            UFL.unite(l,l2)
for r, lis in rmap.items():
    for l in rmap[r]:
        for r2 in lmap[l]:
            UFR.unite(r,r2)

varl = {}
varr = {}

for l in lmap.keys():
    gr = UFL.find(l)
    if gr in varl:
        varl[gr] += 1
    else:
        varl[gr] = 1

for r in rmap.keys():
    gr = UFR.find(r)
    if gr in varr:
        varr[gr] += 1
    else:
        varr[gr] = 1

res = {}
for l, lis in lmap.items():
    gl = UFL.find(l)
    gr = UFR.find(lis[0])
    res[(gl,gr)] = varl[gl] * varr[gr]

# print(varl)
# print(varr)
# print(res)
ressum = 0
for i in res.values():
    ressum += i
print(ressum - N)