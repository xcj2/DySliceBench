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
    s1 = S()
    s2 = S()
    seq = ''
    i = 0
    while i < N:
        if s1[i] == s2[i]:
            seq += 'v'
            i += 1
        else:
            seq += 'h'
            i += 2
    if seq[0] == 'v':
        ans = 3
    else:
        ans = 6

    prev = seq[0]
    for i in range(1, len(seq)):
        cur = seq[i]
        if prev == 'v' and cur == 'h':
            ans *= 2
        if prev == 'v' and cur == 'v':
            ans *= 2
        if prev == 'h' and cur == 'h':
            ans *= 3
        if prev == 'h' and cur == 'v':
            ans *= 1
        prev = cur
        ans %= mod
    print(ans)






main()

