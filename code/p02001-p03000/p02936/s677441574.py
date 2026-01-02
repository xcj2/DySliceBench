import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools, os, pdb
sys.setrecursionlimit(10**7)
inf = 10 ** 20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def _I(): return int(sys.stdin.readline())
def _F(): return float(sys.stdin.readline())
def _pf(s): return print(s, flush=True)
def perr(s):
    if 'LOCAL' in os.environ:
        print(s)

def main():
    global AB, PX, T
    if 'BIG' in os.environ:
        N = 2* 10** 5
        Q = 2 * 10 ** 5
        AB = [[i, i + 1] for i in range(1, N)]
        PX = [[i, 10] for i in range(Q)]
    else:
        N, Q = LI()
        #  AB = []
        T = [[] for _ in range(N+1)]
        PX = [0] * (N+1)
        for i in range(N-1):
            a, b = LI()
            #  AB += (a, b)
            T[a].append(b)
            T[b].append(a)

        for i in range(Q):
            p, x = LI()
            PX[p] += x
        dfs(1, -1)
        print(' '.join(map(lambda x: str(x), PX[1:])))
        #  for i in PX[1:]:
        #      print(i, end=' ')
        #  ans = [0 for _ in range(N)]

def dfs(parent, parent_parent):
    for node in T[parent]:
        if node != parent_parent:
            PX[node] += PX[parent]
            dfs(node, parent)

if __name__ == '__main__':
    main()

