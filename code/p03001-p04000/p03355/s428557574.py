import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 998244353
dd = [(0,-1),(1,0),(0,1),(-1,0)]
ddn = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,-1),(-1,0),(-1,1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)


s = S()
k = I()
n = len(s)
res = []

def push(res,s):
    if s not in res:
        for i in range(len(res)):
            if s<res[i]:
                res.insert(i,s)
                break
        res.append(s)
    return(res[0:k])

for i in range(n):
    for j in range(i,n)[0:5]:
        s1 = s[i:j+1]
        res = push(res,s1)

print(res[-1])

