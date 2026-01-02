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
    X, Y, A, B, C = LI()
    p = sorted(LI())[::-1]
    q = sorted(LI())[::-1]
    r = sorted(LI())[::-1]
    eat = p[:X] + q[:Y]
    eat = sorted(eat)
    r_i = 0
    ans = 0
    for apple in eat:
        if r_i >= C:
            ans += apple
            continue
        if apple < r[r_i]:
            ans += r[r_i]
            r_i += 1
        else:
            ans += apple
    print(ans)


main()

