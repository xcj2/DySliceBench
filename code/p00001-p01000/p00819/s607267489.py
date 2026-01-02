import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 998244353

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
    n = I()
    ni = 0
    d = '0123456789'

    while ni < n:
        ni += 1
        s = S()
        m = S()
        l = len(m)
        for c in s[::-1]:
            if c == 'J':
                m = m[-1] + m[:-1]
            elif c == 'C':
                m = m[1:] + m[0]
            elif c == 'E':
                if l % 2 == 0:
                    m = m[l//2:] + m[:l//2]
                else:
                    m = m[l//2+1:] + m[l//2] + m[:l//2]
            elif c == 'A':
                m = m[::-1]
            elif c == 'P':
                m = ''.join([t if not t in d else d[d.index(t)-1] for t in m])
            elif c == 'M':
                m = ''.join([t if not t in d else d[(d.index(t)+1)%10] for t in m])

        rr.append(m)

    return '\n'.join(map(str, rr))


print(main())


