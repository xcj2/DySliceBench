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
    N = I()
    A = LI()
    colors = [0] * 10
    free = 0
    for a in A:
        i = a // 400
        if i < 8:
            colors[i] += 1
        else:
            free += 1
    cnt = 0
    for c in colors:
        if c > 0:
            cnt += 1
    m = cnt
    if m == 0:
        m += 1
    M = cnt + free
    print(m, M)

def _main():
    N = I()
    A = LI()
    taken = set()
    free = 0
    for a in A:
        if a < 400:
            taken.add('gray')
        elif a < 800:
            taken.add('br')
        elif a < 1200:
            taken.add('green')
        elif a < 1600:
            taken.add('wat')
        elif a < 2000:
            taken.add('blue')
        elif a < 2400:
            taken.add('yellow')
        elif a < 2800:
            taken.add('orange')
        elif a < 3200:
            taken.add('red')
        else:
            free += 1
    minval = len(taken)
    maxval = minval + free
    print(minval, maxval)

main()

