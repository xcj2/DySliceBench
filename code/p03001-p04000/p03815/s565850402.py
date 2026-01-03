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


def solve(x):
    rot = x // (6 + 5)
    res = x % (6 + 5)
    ans = 2 * rot
    # rot:evenなら、つぎに当たるのは6
    if 0 < res <= 6:
        ans += 1
    if 6 < res:
        ans += 2
    return ans

def main():
    x = I()
    ans = solve(x)
    print(ans)
main()

