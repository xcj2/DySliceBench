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
    C, S, F = [], [], []
    for _ in range(N-1):
        c, s, f = LI()
        C.append(c)
        S.append(s)
        F.append(f)
    for i in range(N-1):
        cur_t = 0
        for j in range(i, N-1):
            c, s, f = C[j], S[j], F[j]
            if cur_t > s:
                if cur_t % f == 0:
                    pass
                else:
                    cur_t += (f - cur_t % f)
            else:
                cur_t = s
            cur_t += c
        print(cur_t)
    print(0)
main()

