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
    d = collections.defaultdict(int)
    for _ in range(N):
        s = S()
        d[s] += 1
    v_max = 0
    for k, v in d.items():
        v_max = max(v, v_max)
    sts = []
    for k, v in d.items():
        if v == v_max:
            sts.append(k)
    sts = sorted(sts)
    for string in sts:
        print(string)

main()

