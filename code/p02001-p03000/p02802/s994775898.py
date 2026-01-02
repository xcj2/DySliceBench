import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
     
def main():
    N, M = LI()
    res = [[] for _ in range(N)]
    for _ in range(M):
        p, s = LS()
        p = int(p)
        p -= 1
        res[p].append(s)
    seito = 0
    pena = 0
    for re in res:
        ac = False
        re_pena = 0
        for s in re:
            if s == 'AC':
                seito += 1
                ac = True
                break
            else:
                re_pena += 1
        if ac:
            pena += re_pena
    print(seito, pena)

main()

