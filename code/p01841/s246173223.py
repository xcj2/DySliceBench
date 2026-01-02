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
    a = S()
    b = S()

    def f(s):
        if not s:
            return None
        if s[0] != '(':
            return int(s)
        c = 1
        mi = -1
        for i in range(1, len(s)):
            if s[i] == '(':
                c += 1
            elif s[i] == ')':
                c -= 1
                if c == 0:
                    mi = i
                    break

        c = 1
        ki = -1
        for i in range(mi+2, len(s)):
            if s[i] == '[':
                c += 1
            elif s[i] == ']':
                c -= 1
                if c == 0:
                    ki = i
                    break

        return [f(s[mi+2:ki]), f(s[1:mi]), f(s[ki+2:-1])]

    fa = f(a)
    fb = f(b)
    def g(a, b):
        if a is None or b is None:
            return None
        if isinstance(a, int) or isinstance(b, int):
            ai = a
            while not isinstance(ai, int):
                ai = ai[0]

            bi = b
            while not isinstance(bi, int):
                bi = bi[0]

            return ai + bi

        return [g(a[i],b[i]) for i in range(3)]

    def h(a):
        if a is None:
            return ''
        if isinstance(a, int):
            return str(a)
        return '({})[{}]({})'.format(h(a[1]),h(a[0]),h(a[2]))


    return h(g(fa, fb))


print(main())

