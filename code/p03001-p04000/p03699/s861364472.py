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
    A = []
    for _ in range(N):
        A.append(I())
    A = sorted(A)
    ans = sum(A)
    if ans % 10 != 0:
        print(ans)
        return
    non_10 = [x for x in A if x % 10 > 0]
    if len(non_10) == 0:
        print(0)
        return
    else:
        print(ans - non_10[0])
        return


main()

