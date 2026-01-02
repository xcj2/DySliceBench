import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
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

def main():
    rr = []

    m = {}
    def f(s):
        k = s
        if k in m:
            return m[k]
        t = set(re.findall(r"\([^()]+\)", s))
        while t:
            for c in t:
                s = s.replace(c, f(c[1:-1]))
            t = set(re.findall(r"\([^()]+\)", s))
        while '-' in s:
            s = s.replace('-1', '1')
            s = s.replace('-2', '0')
            s = s.replace('-0', '2')
        r = s[0]
        for i in range(len(s)//2):
            if s[i*2+1] == '*':
                r = min(r,s[i*2+2])
            else:
                r = max(r,s[i*2+2])
        m[k] = r
        return r

    while True:
        s = S()
        if s == '.':
            break

        tr = 0
        for P,Q,R in itertools.product(['0', '1', '2'], repeat=3):
            ts = s.replace('P', P)
            ts = ts.replace('Q', Q)
            ts = ts.replace('R', R)
            if f(ts) == '2':
                tr += 1

        rr.append(tr)

    return '\n'.join(map(str, rr))



print(main())

