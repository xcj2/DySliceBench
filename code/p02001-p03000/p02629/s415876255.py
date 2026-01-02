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
    s = 'abcdefghijklmnopqrstuvwxyz'
    assert len(s) == 26
    cur = []
    while N > 0:
        amari = N % 26
        if amari == 0:
            amari += 26
        cur.append(s[amari-1])
        N -= amari
        N //= 26
    print(''.join(cur[::-1]))
main()

