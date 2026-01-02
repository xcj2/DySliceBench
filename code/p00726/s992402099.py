import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**13
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

    def f(s,n):
        def _f(s, n):
            # print('_f', s,n)
            l = len(s)
            if l == 0 or n < 1:
                return ''
            r = ''
            if '1' <= s[0] <= '9':
                c = int(s[0])
                ti = 1
                for i in range(1,l):
                    ti = i
                    if not ('0' <= s[i] <= '9'):
                        break
                    c *= 10
                    c += int(s[i])
                if s[ti] == '(':
                    k = 1
                    ki = ti+1
                    for i in range(ti+1,l):
                        if s[i] == '(':
                            k += 1
                        elif s[i] == ')':
                            k -= 1
                            if k == 0:
                                ki = i
                                break
                    kr = _f(s[ti+1:ki], n)
                    kl = len(kr)
                    if kl * c >= n:
                        r = kr * (n//kl+1)
                        return r[:n]
                    r = kr * c
                    r += _f(s[ki+1:], n - len(r))
                    return r
                else:
                    r += s[ti] * c
                    if len(r) >= n:
                        return r[:n]
                    r += _f(s[ti+1:], n - len(r))
                    return r
            r = s[0] + _f(s[1:], n - 1)
            return r

        fr = _f(s, n+1)
        # print(len(fr),fr[n:n+1])
        if len(fr) <= n:
            return '0'
        return fr[n]

    while 1:
        s,n = LS()
        if s == '0' and n == '0' :
            break
        rr.append(f(s, int(n)))
        # print('rr', rr[-1])

    return '\n'.join(map(str,rr))


print(main())

