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
    N, C = LI()
    D = []
    c = []
    m0 = collections.defaultdict(int)
    m1 = collections.defaultdict(int)
    m2 = collections.defaultdict(int)
    for _ in range(C):
        D.append(LI())
    for __ in range(N):
        c.append(LI_())
    for row in range(N):
        for col in range(N):
            color = c[row][col]
            if (row + col) % 3 == 0:
                m0[color] += 1
            elif (row + col) % 3 == 1:
                m1[color] += 1
            else:
                m2[color] += 1
    min_cnt = inf
    for c0 in range(C):
        for c1 in range(C):
            for c2 in range(C):
                cnt = 0
                if c0 == c1 or c1 == c2 or c2 == c0:
                    continue

                for orig_c0, num in m0.items():
                    cnt += (D[orig_c0][c0] * num)

                for orig_c1, num in m1.items():
                    cnt += (D[orig_c1][c1] * num)

                for orig_c2, num in m2.items():
                    cnt += (D[orig_c2][c2] * num)
                min_cnt = min(min_cnt, cnt)
    print(min_cnt)
main()

