import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

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

    def f(s):
        t = [int(c) for c in S()]
        a = [t[ord(c) - ord('a')] if c in 'abcd' else c for c in s]

        def ff(a):
            if len(a) == 1:
                return a[0]
            l = len(a)
            for i in range(l-4):
                if a[i] == '[' and a[i+4] == ']':
                    op = a[i+1]
                    b = a[i+2]
                    c = a[i+3]
                    t = -1
                    if op == '+':
                        t = b | c
                    elif op == '*':
                        t = b & c
                    elif op == '^':
                        t = b ^ c
                    return ff(a[:i] + [t] + a[i+5:])
            return -1

        r = ff(a)
        c = 0
        for k in range(10000):
            tt = [k//(10**i)%10 for i in range(4)]
            aa = [tt[ord(c) - ord('a')] if c in 'abcd' else c for c in s]
            kk = ff(aa)
            if kk == r:
                c += 1
        return '{} {}'.format(r,c)

    while 1:
        n = S()
        if n == '.':
            break
        rr.append(f(n))

    return '\n'.join(map(str, rr))


print(main())

