import itertools,sys,collections,math,random,fractions,bisect;sys.setrecursionlimit(10**7)
sr = sys.stdin.readline; P = print; P2 = lambda x: print(*x, sep="\n")
def I(i=0): t = [int(x)-i for x in sr().split()];return t
def S(): t = sr().split(); return t if len(t) > 1 else t[0]
L1,L2,L3,L4, = [],[],[],[]

N, = I()
A = I()
d = dict()
def dd(n):
    if n in d:
        return d[n]
    else:
        if n < 2:
            return 0
        else:
            d[n] = math.factorial(n) // (math.factorial(n - 2) * math.factorial(2))
            return d[n]
c = collections.Counter(A)
total = 0
for e in c.items():
    total += dd(e[1])
for e in A:
    print(total -  dd(c[e]) + dd(c[e]-1))
